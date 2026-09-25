# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.2. Đếm số giá trị null trên từng cột trong một lần quét.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import functions as F

# Dem so gia tri null cua moi cot (mot job duy nhat)
null_counts = df.select([
    F.count(F.when(F.col(c).isNull(), c)).alias(c)
    for c in df.columns
])
null_counts.show()

# Tinh ty le null theo cot de quyet dinh chien luoc xu ly
tong_so_dong = df.count()
ty_le_null = df.select([
    (F.count(F.when(F.col(c).isNull(), c)) / tong_so_dong).alias(c)
    for c in df.columns
])
ty_le_null.show()
