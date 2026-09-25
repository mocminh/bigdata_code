# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.8. Xử lý giá trị thiếu bằng dropna và fillna.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Loai bo cac dong thieu ngay_dat
df_sach = df2.dropna(subset=["ngay_dat"])

# Thay the gia tri thieu theo tung cot
df_thay = df2.fillna({"ngay_dat": "1900-01-01", "so_luong": 0})
