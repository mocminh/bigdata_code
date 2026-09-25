# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.1. Khởi tạo SparkContext và tạo RDD bằng parallelize, textFile.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import SparkSession
# Khoi tao SparkSession o che do local voi 4 luong xu ly
spark = (SparkSession.builder
         .appName("Chuong3-RDD")
         .master("local[4]")
         .getOrCreate())
sc = spark.sparkContext
# Cach 1: phan tan mot collection co san tren Driver
diem_thi = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5, 7.0, 6.0]
rdd_diem = sc.parallelize(diem_thi, numSlices=4)
# Cach 2: doc du lieu tu he thong luu tru ngoai
rdd_log = sc.textFile("hdfs://namenode:9000/data/access.log")
rdd_cucbo = sc.textFile("file:///opt/spark/data/vidu.txt")
print(rdd_diem.getNumPartitions())   # ket qua: 4
print(rdd_diem.take(3))              # [7.5, 8.0, 6.5]
