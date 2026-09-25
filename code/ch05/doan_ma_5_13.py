# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.13. Chuỗi assembler và scaler, fit trên train rồi transform test.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.feature import StandardScaler

# Chia du lieu TRUOC khi hoc bat ky tham so nao
train, test = df_vec.randomSplit([0.8, 0.2], seed=42)

scaler = StandardScaler(
    inputCol="features_raw",
    outputCol="features",
    withMean=True,   # tru trung binh (can vector day du)
    withStd=True     # chia do lech chuan
)
scaler_model = scaler.fit(train)        # hoc mu, sigma tren TRAIN
train_scaled = scaler_model.transform(train)
test_scaled = scaler_model.transform(test)  # ap dung nguyen ven
