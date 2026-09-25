# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.2. Đọc DataFrame từ các tệp CSV, JSON và Parquet.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Doc tep CSV co dong tieu de, tu suy dien kieu du lieu
df_csv = (spark.read
          .option("header", True)
          .option("inferSchema", True)
          .csv("hdfs:///data/donhang.csv"))

# Doc tep JSON va tep Parquet
df_json = spark.read.json("hdfs:///data/khachhang.json")
df_parquet = spark.read.parquet("hdfs:///data/giaodich.parquet")
