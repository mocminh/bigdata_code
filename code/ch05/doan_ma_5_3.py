# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.3. Phân phối tần suất, phân vị xấp xỉ và tương quan.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Phan phoi tan suat cua bien dinh danh
df.groupBy("thanh_pho").count() \
  .orderBy(F.desc("count")) \
  .show(10)

# Phan vi xap xi voi sai so tuong doi 0.01
q1, q2, q3 = df.approxQuantile("thu_nhap",
                               [0.25, 0.5, 0.75], 0.01)
print("Tu phan vi thu nhat:", q1)
print("Trung vi xap xi   :", q2)
print("Tu phan vi thu ba :", q3)

# He so tuong quan Pearson giua hai bien so
r = df.stat.corr("thu_nhap", "chi_tieu")
print("Tuong quan thu nhap - chi tieu:", r)
