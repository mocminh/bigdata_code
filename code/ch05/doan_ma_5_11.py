# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.11. OneHotEncoder cho hai cột nghề nghiệp và thành phố.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.feature import OneHotEncoder

# Gia su thanh_pho da duoc StringIndexer hoa thanh thanh_pho_idx
encoder = OneHotEncoder(
    inputCols=["nghe_nghiep_idx", "thanh_pho_idx"],
    outputCols=["nghe_nghiep_vec", "thanh_pho_vec"],
    dropLast=True
)
model_ohe = encoder.fit(df_idx)
df_ohe = model_ohe.transform(df_idx)

df_ohe.select("nghe_nghiep", "nghe_nghiep_idx",
              "nghe_nghiep_vec").show(5, truncate=False)
# vi du ket qua: ky_su | 1.0 | (4,[1],[1.0])
