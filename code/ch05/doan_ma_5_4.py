# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.4. Lấy mẫu và chuyển sang pandas để trực quan hóa.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Lay mau ngau nhien 1 phan tram, khong hoan lai, seed co dinh
mau = df.sample(withReplacement=False, fraction=0.01, seed=42)
print("Kich thuoc mau:", mau.count())  # kiem tra truoc khi keo ve

pdf = mau.select("tuoi", "thu_nhap", "chi_tieu").toPandas()

import matplotlib.pyplot as plt
pdf["thu_nhap"].hist(bins=50)
plt.xlabel("Thu nhap")
plt.ylabel("Tan suat")
plt.savefig("phan_phoi_thu_nhap.png")
