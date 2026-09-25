# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.1. Cài đặt và khởi tạo PySpark trên Google Colab.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Buoc 1: cai OpenJDK 17 (Spark 3.5 ho tro Java 8/11/17)
!apt-get update -qq
!apt-get install -y -qq openjdk-17-jdk-headless > /dev/null
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"

# Buoc 2: cai dat PySpark tu PyPI (ghim phien ban theo Bang 2.3)
!pip install -q pyspark==3.5.7

# Buoc 3: khoi tao SparkSession o che do cuc bo
from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .master("local[*]")
         .appName("MoiTruongColab")
         .getOrCreate())

# Buoc 4: kiem chung phien ban va chay thu mot phep dem
print("Phien ban Spark:", spark.version)
so_dong = spark.range(1, 10**7).count()
print("Ket qua dem:", so_dong)
