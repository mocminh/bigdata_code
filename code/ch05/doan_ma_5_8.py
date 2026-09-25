# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.8. Lọc ngoại lai theo quy tắc IQR với approxQuantile.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Tinh Q1, Q3 xap xi va suy ra hai nguong loc
q1, q3 = df.approxQuantile("thu_nhap", [0.25, 0.75], 0.01)
iqr = q3 - q1
can_duoi = q1 - 1.5 * iqr
can_tren = q3 + 1.5 * iqr

df_loc = df.filter(
    (F.col("thu_nhap") >= can_duoi) &
    (F.col("thu_nhap") <= can_tren)
)
so_ngoai_lai = df.count() - df_loc.count()
print("So quan sat bi loai:", so_ngoai_lai)
