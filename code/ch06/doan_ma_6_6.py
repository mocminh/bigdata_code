# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.6. Hồi quy GBT dự đoán giá nhà và so sánh với hồi quy tuyến tính.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.regression import GBTRegressor

gbt = GBTRegressor(featuresCol="features", labelCol="gia_nha",
                   maxIter=100, maxDepth=5, stepSize=0.1,
                   seed=42)
gbt_model = gbt.fit(train_hv)

pred_gbt = gbt_model.transform(test_hv)
rmse_eval = RegressionEvaluator(labelCol="gia_nha",
                                predictionCol="prediction",
                                metricName="rmse")
print("RMSE cua GBT:", rmse_eval.evaluate(pred_gbt))

# GBT cung cung cap do quan trong dac trung nhu rung ngau nhien
print(gbt_model.featureImportances)
