# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 2
# Đoạn mã 2.7. Kiểm tra môi trường thực hành sau khi cài theo phiên bản đã ghim.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Colab: chay Doan ma 2.1 truoc (OpenJDK 17, pyspark==3.5.7)
# May tu quan: pip install -r requirements.txt (Bang 2.3)

import os, sys, platform, subprocess
import pyspark, pandas, pyarrow
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()
java_home = os.environ.get("JAVA_HOME", "/usr")
jv = subprocess.run([java_home + "/bin/java", "-version"],
                    text=True, capture_output=True)
java_ver = jv.stderr.splitlines()[0]
print("Python :", sys.version.split()[0], "-", platform.system())
print("Java   :", java_ver)
print("Spark  :", spark.version, "| pyspark", pyspark.__version__)
print("pandas :", pandas.__version__)
print("pyarrow:", pyarrow.__version__)
# Ket qua mong doi: OpenJDK 17, Spark 3.5.7; Python 3.11 khi cai
# theo Bang 2.3 (runtime Colab 9/2026 dung Python 3.13)
