# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.12. Ghi và đọc lại bảng Parquet có phân vùng theo khu vực.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

(df2.write
    .mode("overwrite")
    .partitionBy("khu_vuc")
    .parquet("hdfs:///warehouse/don_hang_parquet"))

# Doc lai: Spark chi quet thu muc phan vung thoa dieu kien loc
df_nam = (spark.read.parquet("hdfs:///warehouse/don_hang_parquet")
          .filter(F.col("khu_vuc") == "Nam"))
df_nam.show()
