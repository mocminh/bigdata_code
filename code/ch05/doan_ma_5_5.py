# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 5
# Đoạn mã 5.5. Phát hiện lệch phân phối và biến đổi logarit.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# He so lech va do nhon cua bien thu nhap
df.select(F.skewness("thu_nhap").alias("do_lech"),
          F.kurtosis("thu_nhap").alias("do_nhon")).show()

# So sanh trung binh voi trung vi xap xi
tb = df.agg(F.mean("thu_nhap")).first()[0]
tv = df.approxQuantile("thu_nhap", [0.5], 0.01)[0]
print("Trung binh:", tb, "- Trung vi:", tv)

# Bien doi logarit lam giam do lech phai
df = df.withColumn("log_thu_nhap", F.log1p(F.col("thu_nhap")))
