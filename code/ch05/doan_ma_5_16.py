# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.16. Lưu và nạp lại PipelineModel.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Luu pipeline da huan luyen xuong HDFS
duong_dan = "hdfs://namenode:9000/models/pipeline_tien_xu_ly"
pipe_model.write().overwrite().save(duong_dan)

# Nap lai o phien lam viec khac (moi truong trien khai)
from pyspark.ml import PipelineModel
pipe_model_2 = PipelineModel.load(duong_dan)
# du_lieu_moi: DataFrame moi, cung luoc do voi du lieu huan luyen
du_lieu_moi_ready = pipe_model_2.transform(du_lieu_moi)
