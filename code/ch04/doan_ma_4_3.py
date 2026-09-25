# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.3. Tạo DataFrame từ RDD với lược đồ StructType tường minh.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql.types import (StructType, StructField,
                               StringType, IntegerType, DoubleType)

rdd = spark.sparkContext.parallelize(
    [("SP01", "Laptop", 25, 1500.0),
     ("SP02", "Ban phim", 120, 25.5)])

schema = StructType([
    StructField("ma_sp", StringType(), False),
    StructField("ten_sp", StringType(), True),
    StructField("ton_kho", IntegerType(), True),
    StructField("gia", DoubleType(), True)])

df_sp = spark.createDataFrame(rdd, schema)
df_sp.printSchema()
