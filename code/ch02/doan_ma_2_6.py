# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.6. Đóng gói môi trường conda và nộp lên cụm YARN.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Tren may phat trien: tao va dong goi moi truong conda
#   conda create -y -n mtspark python=3.11 numpy pandas
#   conda pack -n mtspark -o mtspark.tar.gz

# Khi nop ung dung: gui archive kem theo va tro bien moi truong
#   export PYSPARK_DRIVER_PYTHON=python
#   export PYSPARK_PYTHON=./mt/bin/python
#   spark-submit --master yarn \
#     --archives mtspark.tar.gz#mt \
#     ung_dung.py
