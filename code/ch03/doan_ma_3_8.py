# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.8. Chương trình đếm từ hoàn chỉnh với RDD.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

rdd_vanban = sc.textFile("hdfs://namenode:9000/data/vanban.txt")
rdd_demtu = (rdd_vanban
    .flatMap(lambda dong: dong.lower().split())  # tach thanh tu
    .map(lambda tu: (tu, 1))                     # cap (tu, 1)
    .reduceByKey(lambda a, b: a + b))            # cong theo khoa
# Lay 10 tu pho bien nhat: doi (tu, dem) thanh (dem, tu) roi sap xep
top10 = (rdd_demtu
    .map(lambda cap: (cap[1], cap[0]))
    .sortByKey(ascending=False)
    .take(10))
for dem, tu in top10:
    print("%-15s %d" % (tu, dem))
rdd_demtu.saveAsTextFile("hdfs://namenode:9000/ketqua/demtu")
