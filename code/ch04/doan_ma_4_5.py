# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.5. Khởi tạo tập dữ liệu bán hàng dùng chung cho cả chương.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import functions as F

don_hang = [
    ("D001", "KH01", "Laptop",     "Dien tu",
     2, 1500.0, "2024-03-01", "Bac"),
    ("D002", "KH02", "Dien thoai", "Dien tu",
     5,  800.0, "2024-03-02", "Nam"),
    ("D003", "KH01", "Ao thun",    "Thoi trang",
     10,  12.5, "2024-03-02", "Bac"),
    ("D004", "KH03", "Tu lanh",    "Gia dung",
     1,  950.0, "2024-03-05", "Trung"),
    ("D005", "KH02", "Quan jean",  "Thoi trang",
     3,   45.0, "2024-03-06", "Nam"),
    ("D006", "KH04", "May giat",   "Gia dung",
     2,  700.0, None, "Nam")]

cot = ("ma_don STRING, ma_kh STRING, san_pham STRING, "
       "danh_muc STRING, so_luong INT, don_gia DOUBLE, "
       "ngay_dat STRING, khu_vuc STRING")
df = spark.createDataFrame(don_hang, schema=cot)
df.show()
