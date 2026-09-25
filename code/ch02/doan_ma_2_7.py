# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.7. Cài đặt theo phiên bản đã ghim và kiểm tra môi trường thực hành.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Cai dat dung phien ban da ghim (Colab: dau !, Databricks: %pip)
!pip install -q pyspark==3.5.7 pyarrow==16.1.0 pandas==2.2.2

import sys, platform, subprocess
import pyspark, pandas, pyarrow
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()
jv = subprocess.run(["java", "-version"], text=True,
                    capture_output=True)
java_ver = jv.stderr.splitlines()[0]
print("Python :", sys.version.split()[0], "-", platform.system())
print("Java   :", java_ver)
print("Spark  :", spark.version, "| pyspark", pyspark.__version__)
print("pandas :", pandas.__version__)
print("pyarrow:", pyarrow.__version__)
# Ket qua mong doi: Python 3.11.x, OpenJDK 11 hoac 17, Spark 3.5.7
