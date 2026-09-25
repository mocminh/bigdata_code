# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.14. MinMaxScaler và RobustScaler trên cùng cột vector.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.feature import MinMaxScaler, RobustScaler

# Co gian tuyen tinh ve doan [0, 1]
mm = MinMaxScaler(inputCol="features_raw",
                  outputCol="features_mm")
train_mm = mm.fit(train).transform(train)

# Chuan hoa ben vung theo trung vi va khoang tu phan vi
rb = RobustScaler(inputCol="features_raw",
                  outputCol="features_rb",
                  withCentering=True, withScaling=True)
train_rb = rb.fit(train).transform(train)
