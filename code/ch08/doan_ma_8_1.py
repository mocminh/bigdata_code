# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 8
# Đoạn mã 8.1. Suy luận phân tán mô hình Keras trên Spark bằng mapInPandas.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

import numpy as np
import pandas as pd

MODEL_PATH = "/mnt/models/image_classifier.keras"

def predict_batch(iterator):
    # Nap mo hinh MOT LAN cho moi partition, dung lai cho moi lo
    import tensorflow as tf
    model = tf.keras.models.load_model(MODEL_PATH)
    for pdf in iterator:
        X = np.stack(pdf["features"].to_numpy())
        probs = model.predict(X, batch_size=256, verbose=0)
        yield pd.DataFrame({
            "id": pdf["id"],
            "label_pred": probs.argmax(axis=1),
            "confidence": probs.max(axis=1)})

df_pred = df_features.mapInPandas(
    predict_batch,
    schema="id long, label_pred int, confidence float")
(df_pred.write.mode("overwrite")
    .parquet("hdfs:///output/predictions"))
