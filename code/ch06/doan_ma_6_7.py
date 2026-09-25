# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.7. Đánh giá và so sánh các mô hình phân loại churn.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# So sanh AUC-ROC cua ba mo hinh phan loai da huan luyen
auc_eval = BinaryClassificationEvaluator(
    labelCol="label", rawPredictionCol="rawPrediction",
    metricName="areaUnderROC")
print("AUC Logistic     :", auc_eval.evaluate(pred_lr))
print("AUC Decision Tree:", auc_eval.evaluate(pred_dt))
print("AUC Random Forest:", auc_eval.evaluate(pred_rf))

# Cac do do da lop tren mo hinh rung ngau nhien
mc_eval = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction")
for m in ["accuracy", "f1", "weightedPrecision", "weightedRecall"]:
    v = mc_eval.setMetricName(m).evaluate(pred_rf)
    print(m, "=", round(v, 4))

# Tu xay ma tran nham lan bang phep gom nhom DataFrame
pred_rf.groupBy("label", "prediction").count().show()
