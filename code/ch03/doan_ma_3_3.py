# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.3. Các phép biến đổi cơ bản trên RDD.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

cau_tho = ["gio theo loi gio may duong may",
           "dong nuoc buon thiu hoa bap lay",
           "thuyen ai dau ben song trang do"]
rdd_cau = sc.parallelize(cau_tho, 2)
# map: moi cau cho ra so tu cua cau do (quan he mot-mot)
rdd_sotu = rdd_cau.map(lambda c: len(c.split()))
# flatMap: moi cau sinh ra nhieu tu roi lam phang thanh mot RDD
rdd_tu = rdd_cau.flatMap(lambda c: c.split())
# filter: giu lai cac tu co it nhat 4 ky tu
rdd_tu_dai = rdd_tu.filter(lambda t: len(t) >= 4)
# distinct: loai bo tu trung lap (co xao tron du lieu)
rdd_duynhat = rdd_tu.distinct()
# union: hop voi mot RDD khac cung kieu
rdd_hop = rdd_tu.union(sc.parallelize(["song", "nui"]))
# sample: lay mau ngau nhien khoang 30% so tu, khong hoan lai
rdd_mau = rdd_tu.sample(withReplacement=False,
                        fraction=0.3, seed=42)
print(rdd_sotu.collect())    # [7, 7, 7]
