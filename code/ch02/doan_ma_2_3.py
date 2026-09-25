# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.3. Ứng dụng PySpark hoàn chỉnh: đọc CSV, thống kê và dừng phiên.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Tep: ung_dung_thong_ke.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 1. Khoi tao SparkSession bang builder pattern
spark = (SparkSession.builder
         .master("local[*]")
         .appName("ThongKeDiemThi")
         .config("spark.sql.shuffle.partitions", "8")
         .getOrCreate())

# 2. Doc du lieu CSV co dong tieu de, tu suy dien kieu du lieu
df = (spark.read
      .option("header", True)
      .option("inferSchema", True)
      .csv("diem_thi.csv"))

# 3. Khao sat cau truc va thong ke mo ta
df.printSchema()
df.describe("diem_toan", "diem_van").show()

# 4. Dem so thi sinh va tinh diem trung binh theo tinh
ket_qua = (df.groupBy("ma_tinh")
           .agg(F.count("*").alias("so_thi_sinh"),
                F.round(F.avg("diem_toan"), 2)
                 .alias("diem_tb_toan"))
           .orderBy(F.desc("diem_tb_toan")))
ket_qua.show(10)

# 5. Dung phien lam viec, giai phong tai nguyen
spark.stop()
