# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.7. So sánh groupByKey và reduceByKey trên cùng bài toán.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

rdd_cap = sc.parallelize(
    [("spark", 1), ("hadoop", 1), ("spark", 1),
     ("kafka", 1), ("spark", 1), ("hadoop", 1)], 2)
# Cach 1: groupByKey keo toan bo gia tri cua moi khoa qua mang
kq1 = (rdd_cap.groupByKey()
              .mapValues(lambda ds: sum(ds))
              .collect())
# Cach 2: reduceByKey gop cuc bo o tung partition truoc khi shuffle
kq2 = rdd_cap.reduceByKey(lambda a, b: a + b).collect()
# Hai cach cho cung ket qua nhung chi phi shuffle rat khac nhau
print(sorted(kq1) == sorted(kq2))   # True
