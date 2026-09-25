# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.15. Thay thế UDF bằng hàm dựng sẵn when/otherwise.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

df2.withColumn(
    "loai_don",
    F.when(F.col("thanh_tien").isNull(), "Khong xac dinh")
     .when(F.col("thanh_tien") >= 1000, "Don lon")
     .otherwise("Don thuong")).show()
