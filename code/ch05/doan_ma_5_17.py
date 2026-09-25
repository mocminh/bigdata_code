# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.17. Khung winsorize cho cột thu nhập.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

q1, q3 = df.approxQuantile("thu_nhap", [0.25, 0.75], 0.01)
iqr = q3 - q1
can_duoi, can_tren = q1 - 1.5 * iqr, q3 + 1.5 * iqr
so_ngoai_lai = df.filter((F.col("thu_nhap") < can_duoi) |
                         (F.col("thu_nhap") > can_tren)).count()
df_w = df.withColumn(
    "thu_nhap_w",
    F.when(F.col("thu_nhap") > can_tren, can_tren)
     .when(F.col("thu_nhap") < can_duoi, can_duoi)
     .otherwise(F.col("thu_nhap")))
