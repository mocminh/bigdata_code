# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.1. Tạo DataFrame từ tập hợp cục bộ bằng createDataFrame.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Chuong4-DataFrame") \
    .getOrCreate()

# Tao DataFrame tu danh sach tuple kem chuoi khai bao luoc do
du_lieu = [(1, "Lan", "Ha Noi", 28),
           (2, "Minh", "Da Nang", 35),
           (3, "Hoa", "Can Tho", 41)]
df_nv = spark.createDataFrame(
    du_lieu, schema="ma INT, ten STRING, tinh STRING, tuoi INT")
df_nv.show()
df_nv.printSchema()
