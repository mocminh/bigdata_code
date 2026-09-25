# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 4
# Đoạn mã 4.14. Pandas UDF vector hóa trao đổi dữ liệu qua Apache Arrow.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf("double")
def gia_sau_chiet_khau(thanh_tien: pd.Series) -> pd.Series:
    # Xu ly vector hoa tren tung lo du lieu, khong lap tung hang
    return thanh_tien * 0.95

df2.withColumn("sau_chiet_khau",
               gia_sau_chiet_khau("thanh_tien")).show()
