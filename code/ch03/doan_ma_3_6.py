# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.6. Đo khác biệt thời gian trước và sau khi cache RDD.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

import time
from pyspark import StorageLevel

rdd_gd = (sc.textFile("hdfs://namenode:9000/data/giaodich.csv")
          .map(lambda dong: dong.split(","))
          .filter(lambda tr: tr[3] == "THANH CONG"))
t0 = time.time()
print(rdd_gd.count())              # lan 1: doc va loc lai tu nguon
print("Chua cache: %.2f giay" % (time.time() - t0))
rdd_gd.persist(StorageLevel.MEMORY_AND_DISK)
rdd_gd.count()                     # action nap du lieu vao cache
t1 = time.time()
print(rdd_gd.count())              # doc truc tiep tu bo nho dem
print("Da cache:   %.2f giay" % (time.time() - t1))
rdd_gd.unpersist()                 # giai phong khi khong dung nua
