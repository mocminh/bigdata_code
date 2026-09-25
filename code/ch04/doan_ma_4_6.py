# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.6. Các thao tác select, withColumn, filter/where và orderBy.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# select: chon mot so cot can quan tam
df.select("ma_don", "san_pham", "don_gia").show(3)

# withColumn: them cot thanh_tien = so_luong * don_gia
df2 = df.withColumn("thanh_tien",
                    F.col("so_luong") * F.col("don_gia"))

# filter va where la hai cach viet tuong duong
df2.filter(F.col("thanh_tien") > 1000).show()
df2.where("danh_muc = 'Dien tu' AND so_luong >= 2").show()

# orderBy: sap xep giam dan theo thanh_tien
df2.orderBy(F.col("thanh_tien").desc()).show(5)
