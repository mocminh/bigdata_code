# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 7
# Đoạn mã 7.5. Khung tính bảng RFM và vòng lặp chọn K.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import functions as F
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

rfm = don_hang.groupBy("ma_kh").agg(
    F.datediff(F.lit("2026-07-01"), F.max("ngay_dat"))
     .alias("recency"),
    F.count("*").alias("frequency"),
    F.sum("gia_tri").alias("monetary"))

# Sau khi co df_features (assembler + scaler), thu lan luot cac K
evaluator = ClusteringEvaluator(metricName="silhouette")
for k in range(2, 9):
    model = KMeans(featuresCol="features", k=k,
                   seed=42).fit(df_features)
    sil = evaluator.evaluate(model.transform(df_features))
    print(k, model.summary.trainingCost, sil)
