# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.5. Hồi quy tuyến tính dự đoán giá nhà và đánh giá bằng RegressionEvaluator.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

house_df = spark.read.parquet("hdfs:///data/house_prices.parquet")
train_h, test_h = house_df.randomSplit([0.8, 0.2], seed=42)

house_cols = ["dien_tich", "so_phong_ngu", "so_phong_tam",
              "khoang_cach_trung_tam", "tuoi_nha"]
assembler_h = VectorAssembler(inputCols=house_cols,
                              outputCol="features")
train_hv = assembler_h.transform(train_h)
test_hv = assembler_h.transform(test_h)

lin = LinearRegression(featuresCol="features", labelCol="gia_nha",
                       maxIter=100, regParam=0.1,
                       elasticNetParam=0.5)
lin_model = lin.fit(train_hv)

# Doc tham so hoc duoc: moi he so ung voi mot dac trung
print("Coefficients:", lin_model.coefficients)
print("Intercept   :", lin_model.intercept)

# Danh gia tren tap kiem tra voi RMSE va R2
pred_h = lin_model.transform(test_hv)
evaluator = RegressionEvaluator(labelCol="gia_nha",
                                predictionCol="prediction",
                                metricName="rmse")
print("RMSE:", evaluator.evaluate(pred_h))
print("R2  :", evaluator.setMetricName("r2").evaluate(pred_h))
