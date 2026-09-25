# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.19. Đoạn mã chuẩn hóa có một lỗi phương pháp nghiêm trọng.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

scaler_model = scaler.fit(df_vec)  # hoc tren TOAN BO du lieu
df_scaled = scaler_model.transform(df_vec)
train, test = df_scaled.randomSplit([0.8, 0.2], seed=42)
