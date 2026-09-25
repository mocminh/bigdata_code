# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.3. Huấn luyện cây quyết định và in cấu trúc luật.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.classification import DecisionTreeClassifier

dt = DecisionTreeClassifier(featuresCol="features",
                            labelCol="label",
                            impurity="gini",
                            maxDepth=5,
                            minInstancesPerNode=20,
                            seed=42)
dt_model = dt.fit(train_vec)

# In cau truc cay: tap luat neu-thi doc duoc truc tiep
print(dt_model.toDebugString)

pred_dt = dt_model.transform(test_vec)
pred_dt.select("label", "prediction").show(5)
