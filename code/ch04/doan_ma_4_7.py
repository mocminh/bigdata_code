# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.7. Tổng hợp doanh thu theo danh mục với groupBy và agg.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

bao_cao = (df2.groupBy("danh_muc")
    .agg(F.count("ma_don").alias("so_don"),
         F.sum("thanh_tien").alias("tong_doanh_thu"),
         F.avg("thanh_tien").alias("doanh_thu_tb"),
         F.min("don_gia").alias("gia_thap_nhat"),
         F.max("don_gia").alias("gia_cao_nhat"))
    .orderBy(F.col("tong_doanh_thu").desc()))
bao_cao.show()
