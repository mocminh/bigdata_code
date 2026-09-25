# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 7
# Đoạn mã 7.4. Huấn luyện ALS trên MovieLens và sinh gợi ý.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

ratings = spark.read.csv("hdfs:///data/movielens/ratings.csv",
                         header=True, inferSchema=True) \
                .select("userId", "movieId", "rating")

train, test = ratings.randomSplit([0.8, 0.2], seed=42)

als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating",
          rank=10, regParam=0.1, maxIter=15,
          implicitPrefs=False, coldStartStrategy="drop", seed=42)
als_model = als.fit(train)

# Danh gia RMSE tren tap kiem tra
du_doan = als_model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse",
                                labelCol="rating",
                                predictionCol="prediction")
print("RMSE =", evaluator.evaluate(du_doan))

# Goi y 10 phim tot nhat cho moi nguoi dung
goi_y_user = als_model.recommendForAllUsers(10)
goi_y_user.show(5, truncate=False)

# Goi y 10 nguoi dung tiem nang nhat cho moi phim
goi_y_phim = als_model.recommendForAllItems(10)
