# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.6. Xóa dòng thiếu với dropna: how, thresh và subset.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Xoa dong co bat ky gia tri null nao (mac dinh how="any")
df_a = df.dropna(how="any")

# Chi xoa khi TAT CA cac cot deu null
df_b = df.dropna(how="all")

# Giu lai dong co it nhat 5 gia tri khac null
df_c = df.dropna(thresh=5)

# Chi xet null tren cac cot quan trong doi voi bai toan
df_d = df.dropna(subset=["thu_nhap", "tuoi"])

print("Truoc:", df.count(), "- Sau khi loc:", df_d.count())
