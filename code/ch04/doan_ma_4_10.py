# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.10. Đăng ký khung nhìn tạm và truy vấn bằng spark.sql.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

df2.createOrReplaceTempView("don_hang")

doanh_thu = spark.sql("""
    SELECT danh_muc,
           COUNT(ma_don)             AS so_don,
           SUM(thanh_tien)           AS tong_doanh_thu,
           ROUND(AVG(thanh_tien), 2) AS doanh_thu_tb
    FROM don_hang
    WHERE khu_vuc <> 'Trung'
    GROUP BY danh_muc
    HAVING SUM(thanh_tien) > 500
    ORDER BY tong_doanh_thu DESC
""")
doanh_thu.show()
