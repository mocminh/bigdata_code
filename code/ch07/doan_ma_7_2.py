# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 7
# Đoạn mã 7.2. Quy trình phân cụm khách hàng hoàn chỉnh với Pipeline.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

spark = (SparkSession.builder.appName("PhanCumKhachHang")
         .getOrCreate())

# Cot du lieu: ma_kh, thu_nhap, diem_chi_tieu, so_don_hang
df = spark.read.csv("hdfs:///data/khach_hang.csv",
                    header=True, inferSchema=True)

assembler = VectorAssembler(
    inputCols=["thu_nhap", "diem_chi_tieu", "so_don_hang"],
    outputCol="features_raw")
scaler = StandardScaler(inputCol="features_raw",
                        outputCol="features",
                        withMean=True, withStd=True)
kmeans = KMeans(featuresCol="features", predictionCol="prediction",
                k=3, initMode="k-means||", maxIter=50, seed=42)

pipeline = Pipeline(stages=[assembler, scaler, kmeans])
model = pipeline.fit(df)
du_doan = model.transform(df)

evaluator = ClusteringEvaluator(metricName="silhouette")
print("Silhouette =", evaluator.evaluate(du_doan))

# Dem so khach hang cua tung cum
du_doan.groupBy("prediction").count().orderBy("prediction").show()
