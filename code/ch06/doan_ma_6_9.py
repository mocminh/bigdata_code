# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.9. Quy trình hoàn chỉnh dự đoán khách hàng rời bỏ: từ dữ liệu thô tới mô hình lưu trữ và dự đoán theo lô.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import SparkSession, functions as F
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import (Imputer, StringIndexer,
                                OneHotEncoder, VectorAssembler,
                                StandardScaler)
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import (ParamGridBuilder,
                               TrainValidationSplit)

spark = (SparkSession.builder.appName("Churn-EndToEnd")
         .getOrCreate())

# Buoc 1-2: nap du lieu voi luoc do tuong minh, khao sat nhanh
luoc_do = ("ma_kh STRING, tuoi DOUBLE, goi_cuoc STRING, "
           "khu_vuc STRING, so_thang_su_dung DOUBLE, "
           "cuoc_hang_thang DOUBLE, tong_cuoc DOUBLE, "
           "so_lan_goi_ho_tro DOUBLE, label DOUBLE")
df = (spark.read.option("header", True).schema(luoc_do)
      .csv("hdfs:///data/churn.csv"))
df.groupBy("label").count().show()          # ty le lop
df.select([F.mean(F.col(c).isNull().cast("int")).alias(c)
           for c in df.columns]).show()     # ty le thieu tung cot

# Buoc 3: lam sach toi thieu va chia du lieu TRUOC khi hoc tham so
df = df.dropna(subset=["label", "goi_cuoc", "khu_vuc"])
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)
train_df.cache()

# Buoc 4: dac trung hoa - moi Estimator deu nam trong Pipeline
so_cols = ["tuoi", "so_thang_su_dung", "cuoc_hang_thang",
           "tong_cuoc", "so_lan_goi_ho_tro"]
so_imp = [c + "_imp" for c in so_cols]
imputer = Imputer(inputCols=so_cols, outputCols=so_imp,
                  strategy="median")
dm_cols = ["goi_cuoc", "khu_vuc"]
indexer = StringIndexer(inputCols=dm_cols, handleInvalid="keep",
                        outputCols=[c + "_idx" for c in dm_cols])
encoder = OneHotEncoder(inputCols=[c + "_idx" for c in dm_cols],
                        outputCols=[c + "_vec" for c in dm_cols],
                        handleInvalid="keep")
assembler = VectorAssembler(
    inputCols=so_imp + [c + "_vec" for c in dm_cols],
    outputCol="features_raw")
scaler = StandardScaler(inputCol="features_raw",
                        outputCol="features")

# Buoc 5: mo hinh co so
rf = RandomForestClassifier(featuresCol="features",
                            labelCol="label", seed=42)
pipeline = Pipeline(stages=[imputer, indexer, encoder,
                            assembler, scaler, rf])

# Buoc 6: tinh chinh tiet kiem chi phi bang TrainValidationSplit
grid = (ParamGridBuilder()
        .addGrid(rf.numTrees, [100, 200])
        .addGrid(rf.maxDepth, [6, 10])
        .build())
evaluator = BinaryClassificationEvaluator(
    labelCol="label", metricName="areaUnderROC")
tvs = TrainValidationSplit(estimator=pipeline,
                           estimatorParamMaps=grid,
                           evaluator=evaluator, trainRatio=0.8,
                           parallelism=2, seed=42)
best_model = tvs.fit(train_df).bestModel    # la mot PipelineModel

# Buoc 7: danh gia lan cuoi tren tap kiem tra va dien giai
pred = best_model.transform(test_df)
print("AUC kiem tra:", round(evaluator.evaluate(pred), 4))
pred.groupBy("khu_vuc", "label", "prediction").count().show()
rf_model = best_model.stages[-1]
print("Do quan trong dac trung:", rf_model.featureImportances)

# Buoc 8: luu mo hinh, nap lai va du doan theo lo tren du lieu moi
best_model.write().overwrite().save("hdfs:///models/churn_rf")
model_moi = PipelineModel.load("hdfs:///models/churn_rf")
kh_moi = (spark.read.option("header", True).schema(luoc_do)
          .csv("hdfs:///data/churn_moi.csv"))
(model_moi.transform(kh_moi)
 .select("ma_kh", "prediction", "probability")
 .write.mode("overwrite").parquet("hdfs:///output/du_doan_churn"))
