# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.4. Xem kế hoạch truy vấn bằng explain().
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

df = spark.read.parquet("hdfs:///data/donhang.parquet")
ket_qua = (df.filter(df.khu_vuc == "Nam")
             .select("ma_don", "don_gia")
             .filter(df.don_gia > 100.0))

ket_qua.explain()                 # chi in ke hoach vat ly
ket_qua.explain(mode="extended")  # in du bon giai doan ke hoach
# Trich ke hoach vat ly (rut gon):
# *(1) Project [ma_don, don_gia]
# +- *(1) Filter (isnotnull(khu_vuc) AND isnotnull(don_gia)
#                 AND (khu_vuc = Nam) AND (don_gia > 100.0))
#    +- FileScan parquet [ma_don, don_gia, khu_vuc]
#       PushedFilters: [IsNotNull(khu_vuc), IsNotNull(don_gia),
#                       EqualTo(khu_vuc,Nam),
#                       GreaterThan(don_gia,100.0)]
