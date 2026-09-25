# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 8
# Đoạn mã 8.5. Suy luận phân tán bằng mapInPandas.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

import numpy as np
import pandas as pd

def du_doan(cac_lo):
    import tensorflow as tf
    # nap mo hinh MOT LAN cho moi partition
    model = tf.keras.models.load_model("/mnt/models/model.h5")
    for lo in cac_lo:              # moi lo la mot pandas DataFrame
        X = np.stack(lo["dac_trung"].to_numpy())
        lo["nhan"] = model.predict(X).argmax(axis=1)
        yield lo[["id", "nhan"]]

ketqua = df.mapInPandas(du_doan, schema="id string, nhan int")
ketqua.write.mode("overwrite").parquet("/data/ketqua_du_doan")
