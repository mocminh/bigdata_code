# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 1
# Đoạn mã 1.2. Chuỗi phép biến đổi thống kê lỗi theo địa chỉ IP.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

logs   = sc.textFile("data/access.log")
errs   = logs.filter(lambda line: "ERROR" in line)
pairs  = errs.map(lambda line: (line.split(" ")[0], 1))
counts = pairs.reduceByKey(lambda a, b: a + b)
result = counts.collect()
