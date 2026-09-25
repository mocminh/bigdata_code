# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 7
# Đoạn mã 7.3. Khai phá tập mục phổ biến và luật kết hợp bằng FPGrowth.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.fpm import FPGrowth

giao_dich = spark.createDataFrame([
    (1, ["banh mi", "sua", "trung"]),
    (2, ["banh mi", "sua"]),
    (3, ["trung", "ca phe"]),
    (4, ["banh mi", "sua", "ca phe"]),
    (5, ["ca phe", "trung"]),
    (6, ["banh mi", "trung"]),
], ["ma_gd", "items"])

fp = FPGrowth(itemsCol="items", minSupport=0.3, minConfidence=0.6)
fp_model = fp.fit(giao_dich)

# 1) Cac tap muc pho bien va tan suat xuat hien
tap_pho_bien = fp_model.freqItemsets
tap_pho_bien.orderBy("freq", ascending=False).show(truncate=False)

# 2) Cac luat ket hop kem confidence, lift, support
luat = fp_model.associationRules
luat.orderBy("lift", ascending=False).show(truncate=False)

# 3) Ap luat len tung gio hang de goi y mat hang mua kem
fp_model.transform(giao_dich).show(truncate=False)
