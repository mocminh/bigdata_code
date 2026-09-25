# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 1
# Đoạn mã 1.1. Chương trình đếm từ bằng PySpark.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import SparkSession

# Khoi tao SparkSession - diem vao thong nhat cua ung dung Spark
spark = (SparkSession.builder
         .appName("DemTuPySpark")
         .master("local[*]")
         .getOrCreate())
sc = spark.sparkContext

# Chuoi transformation: chua thuc thi, chi ghi nhan vao DAG
lines = sc.textFile("data/vanban.txt")
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
counts = pairs.reduceByKey(lambda a, b: a + b)

# Action collect() kich hoat viec thuc thi toan bo DAG
for word, freq in counts.collect():
    print(word, freq)

spark.stop()
