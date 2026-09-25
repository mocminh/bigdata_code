# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.12. Hai nhánh phân tích dùng chung một RDD trung gian.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# chuan_hoa: ham lam sach mot dong log, chi phi tinh toan lon
logs = sc.textFile("data/access.log")
errs = logs.filter(lambda d: "ERROR" in d).map(chuan_hoa)

so_loi   = errs.count()
theo_ip  = errs.map(lambda d: (d.split(" ")[0], 1)) \
               .reduceByKey(lambda a, b: a + b).collect()
