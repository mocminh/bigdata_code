# -*- coding: utf-8 -*-
# Giáo trình Dữ liệu lớn – Chương 3
# Đoạn mã 3.9. Kết nối hai tập dữ liệu sinh viên và điểm thi.
# Mã nguyên văn như trong sách (đường dẫn HDFS/Volume); bản chạy trên Colab: chXX.ipynb

# (ma sinh vien, ho ten)
rdd_sv = sc.parallelize([("SV01", "Nguyen Van An"),
                         ("SV02", "Tran Thi Binh"),
                         ("SV03", "Le Van Cuong"),
                         ("SV04", "Pham Thi Dung")])
# (ma sinh vien, diem mon Du lieu lon)
rdd_diem = sc.parallelize([("SV01", 8.5), ("SV02", 7.0),
                           ("SV01", 9.0), ("SV05", 6.5)])
# join (ket noi trong): chi giu khoa co mat o CA HAI phia
print(rdd_sv.join(rdd_diem).collect())
# leftOuterJoin: giu ca sinh vien chua co diem (gia tri None)
print(rdd_sv.leftOuterJoin(rdd_diem).collect())
# cogroup: moi khoa kem hai day gia tri tu hai RDD
gom = rdd_sv.cogroup(rdd_diem)
print([(k, (list(a), list(b))) for k, (a, b) in gom.collect()])
# countByKey: dem so ban ghi theo khoa, tra ve dict tai Driver
print(dict(rdd_diem.countByKey()))
# ket qua: {'SV01': 2, 'SV02': 1, 'SV05': 1}
