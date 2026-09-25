# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 8
# Đoạn mã 8.4. Theo dõi thí nghiệm và đăng ký mô hình Keras với MLflow.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

import mlflow
import mlflow.tensorflow

mlflow.set_experiment("/exp/image-classifier")
mlflow.tensorflow.autolog()   # tu dong log tham so, metric, mo hinh

with mlflow.start_run(run_name="cnn_baseline"):
    mlflow.log_param("batch_size", 128)
    mlflow.log_param("learning_rate", 1e-3)
    history = model.fit(train_ds, validation_data=val_ds, epochs=20)
    best_acc = max(history.history["val_accuracy"])
    mlflow.log_metric("best_val_accuracy", best_acc)
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.tensorflow.log_model(
        model, artifact_path="model",
        registered_model_name="cnn_classifier")

# Nap phien ban dang o giai doan Production tu Model Registry
model_prod = mlflow.pyfunc.load_model(
    "models:/cnn_classifier/Production")
preds = model_prod.predict(new_data)
