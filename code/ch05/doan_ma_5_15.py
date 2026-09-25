# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.15. Pipeline hoàn chỉnh: StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml import Pipeline
from pyspark.ml.feature import (StringIndexer, OneHotEncoder,
                                VectorAssembler, StandardScaler)

idx_nghe = StringIndexer(inputCol="nghe_nghiep",
                         outputCol="nghe_idx",
                         handleInvalid="keep")
idx_tp = StringIndexer(inputCol="thanh_pho",
                       outputCol="tp_idx",
                       handleInvalid="keep")
ohe = OneHotEncoder(inputCols=["nghe_idx", "tp_idx"],
                    outputCols=["nghe_vec", "tp_vec"])
assembler = VectorAssembler(
    inputCols=["tuoi", "thu_nhap", "chi_tieu",
               "nghe_vec", "tp_vec"],
    outputCol="features_raw")
scaler = StandardScaler(inputCol="features_raw",
                        outputCol="features",
                        withMean=True, withStd=True)

pipeline = Pipeline(stages=[idx_nghe, idx_tp, ohe,
                            assembler, scaler])

train, test = df.randomSplit([0.8, 0.2], seed=42)
pipe_model = pipeline.fit(train)   # moi Estimator hoc tren train
train_ready = pipe_model.transform(train)
test_ready = pipe_model.transform(test)
train_ready.select("features").show(3, truncate=False)
