# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.7. Điền khuyết bằng fillna và Imputer với trung vị.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Dien hang so an dinh rieng cho tung cot
df_dien = df.fillna({"thu_nhap": 0.0,
                     "so_don_hang": 0,
                     "thanh_pho": "khong_ro"})

# Imputer: hoc trung vi tren tap huan luyen roi ap dung lai
from pyspark.ml.feature import Imputer

imputer = Imputer(
    inputCols=["tuoi", "thu_nhap"],
    outputCols=["tuoi_imp", "thu_nhap_imp"],
    strategy="median"          # hoac "mean", "mode"
)
model_imp = imputer.fit(df)    # hoc gia tri dien
df_imp = model_imp.transform(df)
model_imp.surrogateDF.show()   # xem gia tri da hoc
