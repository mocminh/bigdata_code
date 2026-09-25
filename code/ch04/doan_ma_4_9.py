# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.9. Các loại join giữa bảng đơn hàng và bảng khách hàng.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

khach_hang = spark.createDataFrame(
    [("KH01", "Nguyen Van An", "Ha Noi"),
     ("KH02", "Tran Thi Binh", "TP HCM"),
     ("KH05", "Le Van Cuong",  "Hue")],
    schema="ma_kh STRING, ten_kh STRING, thanh_pho STRING")

df2.join(khach_hang, on="ma_kh", how="inner").show()
df2.join(khach_hang, on="ma_kh", how="left").show()
df2.join(khach_hang, on="ma_kh", how="full_outer").show()

# Broadcast join: phat tan bang nho toi moi executor
from pyspark.sql.functions import broadcast
df2.join(broadcast(khach_hang), on="ma_kh", how="inner").show()
