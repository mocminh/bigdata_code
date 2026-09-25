# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 6
# Đoạn mã 6.2. Huấn luyện hồi quy logistic dự đoán khách hàng rời bỏ.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression

# Ghep cac cot dac trung thanh mot vector duy nhat
feature_cols = ["tuoi", "so_thang_su_dung",
                "cuoc_hang_thang", "so_lan_goi_ho_tro"]
assembler = VectorAssembler(inputCols=feature_cols,
                            outputCol="features")
train_vec = assembler.transform(train_df)
test_vec = assembler.transform(test_df)

# Khai bao Estimator voi cac sieu tham so co ban
lr = LogisticRegression(featuresCol="features", labelCol="label",
                        maxIter=100, regParam=0.01,
                        elasticNetParam=0.0)

# Huan luyen: fit() tra ve mot Transformer (mo hinh)
lr_model = lr.fit(train_vec)

# Doc he so hoc duoc cua mo hinh
print("He so (coefficients):", lr_model.coefficients)
print("He so chan (intercept):", lr_model.intercept)

# Du doan tren tap kiem tra
pred_lr = lr_model.transform(test_vec)
pred_lr.select("label", "prediction", "probability").show(5)
