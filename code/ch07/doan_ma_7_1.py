# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 7
# Đoạn mã 7.1. Khảo sát WSSSE và hệ số silhouette theo số cụm K.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

evaluator = ClusteringEvaluator(metricName="silhouette",
                                distanceMeasure="squaredEuclidean")

for k in range(2, 11):
    kmeans = KMeans(featuresCol="features", k=k, seed=42)
    model = kmeans.fit(df_features)
    du_doan = model.transform(df_features)
    wssse = model.summary.trainingCost  # ham muc tieu WSSSE
    sil = evaluator.evaluate(du_doan)   # silhouette trung binh
    print("k = %d | WSSSE = %.1f | silhouette = %.3f"
          % (k, wssse, sil))
