# Dữ liệu mẫu

Các tập dữ liệu dùng trong giáo trình. Cột được liệt kê theo đúng tên dùng trong sách.

| Tệp | Dùng ở | Cột / mô tả |
|---|---|---|
| `diem_thi.csv` | Chương 2 | `ma_tinh`, `diem_toan`, `diem_van`, … (điểm thi theo tỉnh) |
| `vanban.txt`, `vidu.txt` | Chương 1, 3 | văn bản không dấu, mỗi dòng một câu (bài đếm từ) |
| `giaodich.csv`, `giaodich.parquet` | Chương 3, 4 | `ma_gd`, `ma_kh`, `so_tien`, `trang_thai` (cột thứ 4: `THANH CONG`, `THAT BAI`, `CHO XU LY`), `thoi_gian` |
| `donhang.csv`, `donhang.parquet` | Chương 4 | `ma_don`, `ma_kh`, `san_pham`, `danh_muc`, `so_luong`, `don_gia`, `ngay_dat`, `khu_vuc` |
| `khachhang.json` | Chương 4 | `ma_kh`, `ten_kh`, `thanh_pho` |
| `khach_hang` (Parquet, bản thô có giá trị thiếu và ngoại lai) | Chương 5 | `ma_kh`, `tuoi`, `thu_nhap`, `chi_tieu`, `nghe_nghiep`, `thanh_pho`, `so_don_hang`, `diem_chi_tieu` |
| `khach_hang.csv` (bản sạch) | Chương 7 | cùng lược đồ, không có giá trị thiếu, dùng cho phân cụm |
| `don_hang.csv` | Bài 7.1 | `ma_kh`, `ngay_dat`, `gia_tri` (lịch sử đơn hàng cho mô hình RFM) |
| `access.log` | Chương 1, 3 | `<ip> <thời gian>\t<mức>\t<thông điệp>` – tách được bằng `split(" ")[0]` (IP) và `split("\t")[2]` (thông điệp) |
| `churn.csv`, `churn.parquet`, `churn_moi.csv` | Bài 5.2, Chương 6 | `ma_kh`, `tuoi`, `goi_cuoc`, `khu_vuc`, `so_thang_su_dung`, `cuoc_hang_thang`, `tong_cuoc`, `so_lan_goi_ho_tro`, `label` |
| `house_prices.parquet` | Chương 6 | `dien_tich`, `so_phong_ngu`, `so_phong_tam`, `khoang_cach_trung_tam`, `tuoi_nha`, `gia_nha` |
| `movielens/ratings.csv` | Chương 7 | `userId`, `movieId`, `rating`, `timestamp` – tải bộ *ml-latest-small* từ https://grouplens.org/datasets/movielens/ (Harper & Konstan, 2015) |

Toàn bộ tệp (trừ MovieLens) được sinh bằng `generate_data.py` (dữ liệu mô phỏng, seed 2026, có thể tái lập); `churn.csv` có khoảng 2% giá trị thiếu ở `tuoi` và `cuoc_hang_thang` (dùng cho Imputer ở Bài 5.2 và Đoạn mã 6.9), `churn.parquet` là bản đã bỏ giá trị thiếu; `churn_moi.csv` gồm 500 khách hàng mới chưa có nhãn.
