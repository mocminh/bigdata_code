# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.12. VectorAssembler gom các cột thành vector features.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols=["tuoi", "thu_nhap", "chi_tieu",
               "nghe_nghiep_vec", "thanh_pho_vec"],
    outputCol="features_raw",
    handleInvalid="skip"
)
df_vec = assembler.transform(df_ohe)
df_vec.select("features_raw").show(3, truncate=False)
