# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.11. Khung nhìn tạm toàn cục và truy vấn join bằng SQL.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

khach_hang.createGlobalTempView("khach_hang")

spark.sql("""
    SELECT d.ma_don, k.ten_kh, d.san_pham, d.thanh_tien
    FROM don_hang d
    JOIN global_temp.khach_hang k ON d.ma_kh = k.ma_kh
    ORDER BY d.thanh_tien DESC
""").show()
