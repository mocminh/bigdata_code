# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.8. Quy trình tinh chỉnh hoàn chỉnh với Pipeline, ParamGridBuilder và CrossValidator.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Buoc 1: dong goi tien xu ly va thuat toan vao Pipeline
assembler = VectorAssembler(inputCols=feature_cols,
                            outputCol="features")
rf = RandomForestClassifier(featuresCol="features",
                            labelCol="label", seed=42)
pipeline = Pipeline(stages=[assembler, rf])

# Buoc 2: xay luoi tham so (3 x 3 = 9 to hop)
grid = ParamGridBuilder() \
    .addGrid(rf.numTrees, [50, 100, 200]) \
    .addGrid(rf.maxDepth, [5, 8, 12]) \
    .build()

# Buoc 3: khai bao bo danh gia va CrossValidator
evaluator = BinaryClassificationEvaluator(
    labelCol="label", metricName="areaUnderROC")
cv = CrossValidator(estimator=pipeline,
                    estimatorParamMaps=grid,
                    evaluator=evaluator,
                    numFolds=5,
                    parallelism=4,
                    seed=42)

# Buoc 4: 9 x 5 = 45 lan fit + 1 lan fit lai tren tap huan luyen
cv_model = cv.fit(train_df)

# Buoc 5: trich xuat mo hinh va tham so tot nhat
best_rf = cv_model.bestModel.stages[-1]
print("numTrees tot nhat:", best_rf.getNumTrees)
print("maxDepth tot nhat:", best_rf.getMaxDepth())
print("AUC trung binh tot nhat:", max(cv_model.avgMetrics))

# Buoc 6: danh gia lan cuoi tren tap kiem tra doc lap
pred_best = cv_model.transform(test_df)
print("AUC tren tap kiem tra:", evaluator.evaluate(pred_best))
