# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.1. Khởi tạo phiên làm việc và chia dữ liệu huấn luyện/kiểm tra.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Chuong6-MLlib") \
    .getOrCreate()

# Doc du lieu khach hang vien thong tu HDFS
df = spark.read.parquet("hdfs:///data/churn.parquet")

# Chia ngau nhien: 80% huan luyen, 20% kiem tra
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

print("So ban ghi huan luyen:", train_df.count())
print("So ban ghi kiem tra :", test_df.count())
