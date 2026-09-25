# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 7
# Đoạn mã 7.6. Khung lời giải bài tập ALS.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.recommendation import ALS

ratings = spark.createDataFrame([
    (1, 101, 5.0), (1, 102, 4.5), (1, 103, 1.0), (1, 105, 4.0),
    (2, 101, 4.5), (2, 102, 4.0), (2, 104, 1.5),
    (3, 102, 1.0), (3, 103, 4.5), (3, 104, 5.0), (3, 105, 1.5),
    (4, 101, 1.5), (4, 103, 4.0), (4, 104, 4.5),
], ["userId", "movieId", "rating"])

als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating",
          rank=5, regParam=0.1, maxIter=10,
          coldStartStrategy="drop", seed=42)
als_model = als.fit(ratings)

cap_can_du_doan = spark.createDataFrame(
    [(2, 105), (4, 102)], ["userId", "movieId"])
als_model.transform(cap_can_du_doan).show()

als_model.recommendForAllUsers(2).show(truncate=False)
