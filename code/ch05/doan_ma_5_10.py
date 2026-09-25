# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.10. StringIndexer và IndexToString trên cột nghề nghiệp.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.ml.feature import StringIndexer, IndexToString

indexer = StringIndexer(
    inputCol="nghe_nghiep",
    outputCol="nghe_nghiep_idx",
    handleInvalid="keep"   # nhan la duoc gom vao chi so cuoi
)
model_idx = indexer.fit(df_train)      # hoc bang tan suat
df_idx = model_idx.transform(df_train)

# Danh sach nhan theo thu tu tan suat giam dan
print(model_idx.labelsArray[0])
# vi du: ['nhan_vien', 'ky_su', 'giao_vien', 'bac_si', ...]

# Chuyen nguoc chi so ve nhan goc khi dien giai ket qua
inverter = IndexToString(
    inputCol="nghe_nghiep_idx",
    outputCol="nghe_nghiep_goc",
    labels=model_idx.labelsArray[0]
)
df_goc = inverter.transform(df_idx)
