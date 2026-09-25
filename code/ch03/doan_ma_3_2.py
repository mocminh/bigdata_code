# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.2. Kiểm tra và điều chỉnh số partition của RDD.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

rdd_a = sc.parallelize(range(1, 100001))    # dung gia tri mac dinh
print(rdd_a.getNumPartitions())             # thuong = so loi CPU
rdd_b = sc.parallelize(range(1, 100001), 8) # chi dinh 8 partition
# repartition: tang/giam so partition, gay shuffle toan bo du lieu
rdd_16 = rdd_b.repartition(16)
# coalesce: giam so partition bang cach gop, tranh duoc shuffle
rdd_4 = rdd_16.coalesce(4)
print(rdd_16.getNumPartitions(), rdd_4.getNumPartitions())   # 16 4
