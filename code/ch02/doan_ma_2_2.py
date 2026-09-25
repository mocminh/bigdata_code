# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.2. Đọc tệp CSV đã tải lên volume trong notebook Databricks.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Tren Databricks, doi tuong spark da duoc khoi tao san
df = (spark.read
      .option("header", True)
      .option("inferSchema", True)
      .csv("/Volumes/workspace/default/du_lieu/diem_thi.csv"))
df.show(5)
