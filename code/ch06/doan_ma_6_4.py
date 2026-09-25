# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.4. Huấn luyện rừng ngẫu nhiên và xem độ quan trọng đặc trưng.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.classification import RandomForestClassifier

rf = RandomForestClassifier(featuresCol="features",
                            labelCol="label",
                            numTrees=100,
                            maxDepth=8,
                            featureSubsetStrategy="sqrt",
                            seed=42)
rf_model = rf.fit(train_vec)

# Do quan trong cua tung dac trung (tong bang 1)
importances = rf_model.featureImportances.toArray()
for name, score in zip(feature_cols, importances):
    print(name, "->", round(float(score), 4))

pred_rf = rf_model.transform(test_vec)
