# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.18. Khung pipeline tiền xử lý cho bài toán churn.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import (Imputer, StringIndexer,
    OneHotEncoder, VectorAssembler, StandardScaler)

df = spark.read.csv("hdfs:///data/churn.csv",
                    header=True, inferSchema=True)
train, test = df.randomSplit([0.8, 0.2], seed=42)

imp = Imputer(inputCols=["tuoi", "cuoc_hang_thang"],
              outputCols=["tuoi_imp", "cuoc_imp"],
              strategy="median")
idx = StringIndexer(inputCols=["goi_cuoc", "khu_vuc"],
                    outputCols=["goi_idx", "kv_idx"],
                    handleInvalid="keep")
ohe = OneHotEncoder(inputCols=["goi_idx", "kv_idx"],
                    outputCols=["goi_vec", "kv_vec"])
asm = VectorAssembler(
    inputCols=["tuoi_imp", "so_thang_su_dung", "cuoc_imp",
               "so_lan_goi_ho_tro", "goi_vec", "kv_vec"],
    outputCol="features_raw", handleInvalid="skip")
scl = StandardScaler(inputCol="features_raw", outputCol="features",
                     withMean=True, withStd=True)

pipe = Pipeline(stages=[imp, idx, ohe, asm, scl])
model = pipe.fit(train)              # chi hoc tren train
train_ready = model.transform(train)
test_ready = model.transform(test)
model.write().overwrite().save("models/pipe_churn")
model2 = PipelineModel.load("models/pipe_churn")
