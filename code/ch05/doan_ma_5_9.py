# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.9. Winsorize giá trị vượt ngưỡng bằng when/otherwise.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

df_wins = df.withColumn(
    "thu_nhap_w",
    F.when(F.col("thu_nhap") > can_tren, can_tren)
     .when(F.col("thu_nhap") < can_duoi, can_duoi)
     .otherwise(F.col("thu_nhap"))
)
df_wins.select("thu_nhap", "thu_nhap_w").describe().show()
