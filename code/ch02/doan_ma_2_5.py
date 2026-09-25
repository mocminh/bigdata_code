# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.5. Phân phối mã nguồn dùng chung cho các executor.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Cach 1: khai bao khi nop ung dung
#   spark-submit --py-files tien_ich.zip ung_dung.py

# Cach 2: them tep ngay trong luc chay
spark.sparkContext.addPyFile("tien_ich.zip")
from tien_ich import chuan_hoa_ten  # ham nay dung duoc trong UDF
