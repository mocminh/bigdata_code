# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.13. Định nghĩa và đăng ký UDF cho DataFrame API và cho SQL.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def phan_loai(gia_tri):
    if gia_tri is None:
        return "Khong xac dinh"
    if gia_tri >= 1000:
        return "Don lon"
    return "Don thuong"

# Dang ky cho DataFrame API
phan_loai_udf = udf(phan_loai, StringType())
df2.withColumn("loai_don",
               phan_loai_udf(F.col("thanh_tien"))).show()

# Dang ky them ten ham de goi trong cau lenh SQL
spark.udf.register("PHAN_LOAI", phan_loai, StringType())
spark.sql("""
    SELECT ma_don, thanh_tien, PHAN_LOAI(thanh_tien) AS loai_don
    FROM don_hang
""").show()
