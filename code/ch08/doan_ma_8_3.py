# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 8
# Đoạn mã 8.3. Khung huấn luyện Keras phân tán với Horovod.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

import tensorflow as tf
import horovod.tensorflow.keras as hvd

hvd.init()                          # 1. Khoi tao Horovod

# 2. Gan (pin) moi tien trinh voi mot GPU cuc bo
gpus = tf.config.list_physical_devices("GPU")
if gpus:
    tf.config.set_visible_devices(gpus[hvd.local_rank()], "GPU")

model = build_model()
# 3. Scale learning rate theo so worker
opt = tf.keras.optimizers.SGD(learning_rate=0.01 * hvd.size())
# 4. Boc optimizer de dong bo gradient bang All-Reduce
opt = hvd.DistributedOptimizer(opt)
model.compile(optimizer=opt,
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

callbacks = [
    # 5. Phat trong so ban dau tu rank 0 toi moi worker
    hvd.callbacks.BroadcastGlobalVariablesCallback(0),
    hvd.callbacks.MetricAverageCallback(),
]
if hvd.rank() == 0:                 # chi rank 0 ghi checkpoint
    callbacks.append(
        tf.keras.callbacks.ModelCheckpoint("/mnt/ckpt/best.keras"))

model.fit(train_dataset, epochs=20, callbacks=callbacks,
          verbose=1 if hvd.rank() == 0 else 0)
