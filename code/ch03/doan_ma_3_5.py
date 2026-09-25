# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.5. Các action thông dụng trên RDD.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

rdd_diem = sc.parallelize([7.5, 8.0, 6.5, 9.0, 5.5, 8.5], 3)
print(rdd_diem.count())      # 6: tong so phan tu
print(rdd_diem.first())      # 7.5: phan tu dau tien
print(rdd_diem.take(4))      # [7.5, 8.0, 6.5, 9.0]
print(rdd_diem.collect())    # keo TOAN BO du lieu ve Driver
# reduce voi ham cong: tinh tong roi suy ra diem trung binh
tong = rdd_diem.reduce(lambda a, b: a + b)
print("Diem trung binh:", tong / rdd_diem.count())
# Ghi ket qua xuong HDFS, moi partition mot tep part-xxxxx
rdd_diem.saveAsTextFile("hdfs://namenode:9000/ketqua/diem")
# foreach chay ngay tai Executor; print nam trong log Executor
rdd_diem.foreach(lambda x: print(x))
