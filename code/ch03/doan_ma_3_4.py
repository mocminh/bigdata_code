# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.4. Chuỗi biến đổi chỉ được thực thi khi gặp action.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# Ba dong duoi day hoan tat tuc thi, ke ca voi tep hang tram GB,
# vi chua co bat ky tinh toan nao duoc thuc hien
rdd_log = sc.textFile("hdfs://namenode:9000/data/access.log")
rdd_loi = rdd_log.filter(lambda dong: "ERROR" in dong)
rdd_thongdiep = rdd_loi.map(lambda dong: dong.split("\t")[2])
# In pha he (lineage) de quan sat chuoi phu thuoc giua cac RDD
print(rdd_thongdiep.toDebugString().decode("utf-8"))
# Action moi la thoi diem Spark xay DAG, toi uu va thuc thi
so_loi = rdd_thongdiep.count()
nam_dong_dau = rdd_thongdiep.take(5)   # chi quet du lieu vua du
