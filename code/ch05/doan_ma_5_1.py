# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.1. Thống kê mô tả với describe và summary.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Doc du lieu khach hang tu HDFS
df = spark.read.parquet("hdfs://namenode:9000/data/khach_hang")
print("So dong:", df.count(), "- So cot:", len(df.columns))
df.printSchema()

# Nam thong ke co ban cho cac cot so
df.describe("tuoi", "thu_nhap", "chi_tieu").show()

# summary cho phep chi dinh them cac phan vi
df.select("tuoi", "thu_nhap") \
  .summary("count", "mean", "stddev", "min",
           "25%", "50%", "75%", "max") \
  .show()
