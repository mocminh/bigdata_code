# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.4. Nộp ứng dụng lên cụm YARN bằng spark-submit.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Lenh chay tren terminal cua may client
spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --num-executors 4 \
  --executor-memory 4g \
  --executor-cores 2 \
  ung_dung_thong_ke.py
