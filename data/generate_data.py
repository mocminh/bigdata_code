# -*- coding: utf-8 -*-
"""Sinh lại toàn bộ dữ liệu mẫu của giáo trình Dữ liệu lớn (có thể tái lập, seed = 2026).

Chạy:  python data/generate_data.py            (từ thư mục gốc của kho)
Các tệp được sinh ra đúng lược đồ mà các đoạn mã trong sách sử dụng (xem data/README.md).
Dữ liệu là dữ liệu mô phỏng, chỉ phục vụ học tập.
"""
import json
import os
import random
from datetime import date, datetime, timedelta

import numpy as np
import pandas as pd

SEED = 2026
rng = np.random.default_rng(SEED)
random.seed(SEED)
HERE = os.path.dirname(os.path.abspath(__file__))


def out(name):
    return os.path.join(HERE, name)


# ----------------------------------------------------------------------------- Chương 1, 3
def gen_vanban():
    with open(out("vanban.txt"), "w", encoding="utf-8") as f:
        f.write("spark xu ly du lieu lon\ndu lieu lon can xu ly phan tan\nspark giu du lieu trong bo nho\n")
    with open(out("vidu.txt"), "w", encoding="utf-8") as f:
        f.write("day la tep vi du doc tu he thong tep cuc bo\nmoi dong la mot phan tu cua rdd\n")


def gen_access_log(n=20000):
    """Nhật ký máy chủ: '<ip> <thoi_gian>\\t<muc>\\t<thong_diep>' (khớp split(' ')[0] và split('\\t')[2])."""
    ips = [f"10.0.{rng.integers(0, 8)}.{rng.integers(1, 255)}" for _ in range(60)]
    weights = rng.dirichlet(np.ones(60) * 0.7)
    levels = ["INFO", "INFO", "INFO", "INFO", "WARN", "ERROR"]
    paths = ["/index.html", "/api/login", "/api/orders", "/static/app.js", "/checkout", "/search?q=spark"]
    errors = ["Timeout khi goi dich vu thanh toan", "Ket noi CSDL bi tu choi", "Loi 500 tai /api/orders",
              "Het bo nho dem", "Xac thuc that bai", "Tep cau hinh khong ton tai"]
    t0 = datetime(2026, 3, 1, 0, 0, 0)
    with open(out("access.log"), "w", encoding="utf-8") as f:
        for i in range(n):
            ip = ips[rng.choice(60, p=weights)]
            t = t0 + timedelta(seconds=int(i * 4.3 + rng.integers(0, 4)))
            lv = levels[rng.integers(0, len(levels))]
            if lv == "ERROR":
                msg = errors[rng.integers(0, len(errors))]
            else:
                msg = f"GET {paths[rng.integers(0, len(paths))]} {200 if lv == 'INFO' else 404} {rng.integers(80, 9000)}"
            f.write(f"{ip} {t.isoformat()}\t{lv}\t{msg}\n")


def gen_giaodich(n=20000):
    """Giao dịch: ma_gd, ma_kh, so_tien, trang_thai (cột thứ 4), thoi_gian."""
    trang_thai = rng.choice(["THANH CONG", "THAT BAI", "CHO XU LY"], size=n, p=[0.82, 0.12, 0.06])
    df = pd.DataFrame({
        "ma_gd": [f"GD{i:06d}" for i in range(1, n + 1)],
        "ma_kh": [f"KH{rng.integers(1, 3001):05d}" for _ in range(n)],
        "so_tien": np.round(rng.lognormal(mean=13.0, sigma=0.9, size=n) / 1000) * 1000,
        "trang_thai": trang_thai,
        "thoi_gian": [(datetime(2026, 1, 1) + timedelta(minutes=int(m))).strftime("%Y-%m-%d %H:%M:%S")
                      for m in np.sort(rng.integers(0, 60 * 24 * 180, size=n))],
    })
    df.to_csv(out("giaodich.csv"), index=False)
    df.to_parquet(out("giaodich.parquet"), index=False)


# ----------------------------------------------------------------------------- Chương 2
def gen_diem_thi(n=6000):
    tinh = [f"{i:02d}" for i in range(1, 64)]
    ma_tinh = rng.choice(tinh, size=n)
    df = pd.DataFrame({
        "so_bao_danh": [f"{m}{i:06d}" for i, m in enumerate(ma_tinh, 1)],
        "ma_tinh": ma_tinh,
        "diem_toan": np.clip(np.round(rng.normal(6.4, 1.6, n) * 4) / 4, 0, 10),
        "diem_van": np.clip(np.round(rng.normal(6.8, 1.2, n) * 4) / 4, 0, 10),
        "diem_anh": np.clip(np.round(rng.normal(5.6, 1.9, n) * 4) / 4, 0, 10),
    })
    df.to_csv(out("diem_thi.csv"), index=False)


# ----------------------------------------------------------------------------- Chương 4
def gen_donhang(n=5000):
    san_pham = {"Laptop": ("Dien tu", 1500.0), "Dien thoai": ("Dien tu", 800.0), "Tai nghe": ("Dien tu", 45.0),
                "Ao thun": ("Thoi trang", 12.5), "Quan jean": ("Thoi trang", 35.0), "Giay the thao": ("Thoi trang", 60.0),
                "Sach Spark": ("Sach", 25.0), "Sach Python": ("Sach", 20.0), "Noi com dien": ("Gia dung", 55.0),
                "May xay": ("Gia dung", 40.0)}
    ten_sp = list(san_pham)
    khach = [f"KH{i:02d}" for i in range(1, 41)]
    rows = []
    d0 = date(2024, 3, 1)
    for i in range(1, n + 1):
        sp = ten_sp[rng.integers(0, len(ten_sp))]
        dm, gia = san_pham[sp]
        rows.append({
            "ma_don": f"D{i:05d}",
            "ma_kh": khach[rng.integers(0, len(khach))],
            "san_pham": sp,
            "danh_muc": dm,
            "so_luong": int(rng.integers(1, 12)) if dm != "Dien tu" else int(rng.integers(1, 4)),
            "don_gia": float(np.round(gia * rng.uniform(0.9, 1.1), 1)),
            "ngay_dat": (d0 + timedelta(days=int(rng.integers(0, 365)))).isoformat(),
            "khu_vuc": rng.choice(["Bac", "Trung", "Nam"], p=[0.4, 0.2, 0.4]),
        })
    df = pd.DataFrame(rows)
    df.to_csv(out("donhang.csv"), index=False)
    df.to_parquet(out("donhang.parquet"), index=False)
    # khach hang (JSON Lines) - mot so khach khong co don, mot so don khong co khach (KH05...)
    tp = ["Ha Noi", "TP HCM", "Da Nang", "Hue", "Can Tho", "Hai Phong"]
    ho = ["Nguyen Van", "Tran Thi", "Le Van", "Pham Thi", "Hoang Van", "Vu Thi", "Dang Van", "Bui Thi"]
    ten = ["An", "Binh", "Cuong", "Dung", "Giang", "Hoa", "Khanh", "Lan", "Minh", "Nam", "Phuong", "Quang", "Son", "Thao"]
    with open(out("khachhang.json"), "w", encoding="utf-8") as f:
        for i in range(1, 36):
            rec = {"ma_kh": f"KH{i:02d}", "ten_kh": f"{ho[rng.integers(0, len(ho))]} {ten[rng.integers(0, len(ten))]}",
                   "thanh_pho": tp[rng.integers(0, len(tp))]}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def gen_don_hang_rfm(n=30000):
    """Bài 7.1: don_hang.csv gồm ma_kh, ngay_dat, gia_tri."""
    n_kh = 2500
    tan_suat = rng.gamma(2.0, 6.0, n_kh)          # khach hang mua nhieu / it
    ma_kh_all = rng.choice(np.arange(1, n_kh + 1), size=n, p=tan_suat / tan_suat.sum())
    d0 = date(2025, 7, 1)
    df = pd.DataFrame({
        "ma_kh": [f"KH{k:05d}" for k in ma_kh_all],
        "ngay_dat": [(d0 + timedelta(days=int(rng.integers(0, 365)))).isoformat() for _ in range(n)],
        "gia_tri": np.round(rng.lognormal(mean=12.2, sigma=0.8, size=n) / 1000) * 1000,
    })
    df.sort_values("ngay_dat").to_csv(out("don_hang.csv"), index=False)


# ----------------------------------------------------------------------------- Chương 5, 7
def gen_khach_hang(n=20000):
    nghe = rng.choice(["nhan_vien", "ky_su", "giao_vien", "bac_si", "kinh_doanh", "sinh_vien"],
                      size=n, p=[0.3, 0.2, 0.15, 0.08, 0.17, 0.10])
    tp = rng.choice(["Ha Noi", "TP HCM", "Da Nang", "Can Tho", "Hai Phong"], size=n, p=[0.3, 0.38, 0.12, 0.1, 0.1])
    tuoi = np.clip(rng.normal(36, 11, n).round(), 18, 75)
    he_so = {"nhan_vien": 1.0, "ky_su": 1.5, "giao_vien": 0.9, "bac_si": 1.8, "kinh_doanh": 1.6, "sinh_vien": 0.35}
    thu_nhap = np.array([rng.lognormal(mean=np.log(15 * he_so[g]), sigma=0.45) for g in nghe])   # trieu dong / thang
    thu_nhap = np.round(thu_nhap, 1)
    chi_tieu = np.round(np.clip(thu_nhap * rng.uniform(0.35, 0.85, n) + rng.normal(0, 1.5, n), 0.5, None), 1)
    so_don_hang = rng.poisson(np.clip(chi_tieu / 4, 0.3, 30)).astype(int)
    diem_chi_tieu = np.clip(np.round(100 * chi_tieu / (thu_nhap + 1e-9) * rng.uniform(0.8, 1.2, n)), 1, 100)
    df = pd.DataFrame({
        "ma_kh": [f"KH{i:05d}" for i in range(1, n + 1)],
        "tuoi": tuoi.astype("float64"),
        "thu_nhap": thu_nhap,
        "chi_tieu": chi_tieu,
        "nghe_nghiep": nghe,
        "thanh_pho": tp,
        "so_don_hang": so_don_hang,
        "diem_chi_tieu": diem_chi_tieu,
    })
    # ban sach dung cho phan cum (Chuong 7): khong thieu, khong ngoai lai
    df.to_csv(out("khach_hang.csv"), index=False)
    # ban tho dung cho tien xu ly (Chuong 5): gia tri thieu, ngoai lai, nhieu
    tho = df.copy()
    idx = rng.choice(n, size=int(0.03 * n), replace=False); tho.loc[idx, "thu_nhap"] = np.nan
    idx = rng.choice(n, size=int(0.02 * n), replace=False); tho.loc[idx, "tuoi"] = np.nan
    idx = rng.choice(n, size=int(0.015 * n), replace=False); tho.loc[idx, "thanh_pho"] = None
    idx = rng.choice(n, size=int(0.01 * n), replace=False); tho.loc[idx, "so_don_hang"] = np.nan
    idx = rng.choice(n, size=25, replace=False); tho.loc[idx, "thu_nhap"] = np.round(rng.uniform(900, 3200, 25))  # nhap sai
    tho["so_don_hang"] = tho["so_don_hang"].astype("Int64")
    tho.to_parquet(out("khach_hang"), index=False)          # thu muc/tep parquet 'khach_hang'


# ----------------------------------------------------------------------------- Chương 6
def gen_churn(n=20000):
    goi = rng.choice(["co_ban", "tieu_chuan", "cao_cap"], size=n, p=[0.45, 0.35, 0.2])
    khu_vuc = rng.choice(["Bac", "Trung", "Nam"], size=n, p=[0.38, 0.22, 0.4])
    tuoi = np.clip(rng.normal(38, 12, n).round(), 18, 80)
    so_thang = np.clip(rng.exponential(24, n).round(), 1, 120)
    cuoc = {"co_ban": 120, "tieu_chuan": 250, "cao_cap": 520}
    cuoc_hang_thang = np.round(np.array([cuoc[g] for g in goi]) * rng.uniform(0.8, 1.3, n) / 10) * 10
    so_lan_goi = rng.poisson(1.2, n) + (rng.random(n) < 0.15) * rng.integers(3, 9, n)
    # xac suat roi bo: cang moi, cang goi ho tro nhieu, cuoc cao so voi goi -> cang de roi bo
    z = (-1.1 - 0.035 * (so_thang - 6) + 0.45 * so_lan_goi + 0.002 * (cuoc_hang_thang - 250)
         + np.where(goi == "co_ban", 0.3, 0) + np.where(khu_vuc == "Trung", 0.15, 0) + rng.normal(0, 0.6, n))
    p = 1 / (1 + np.exp(-z))
    label = (rng.random(n) < p).astype(float)
    df = pd.DataFrame({
        "ma_kh": [f"KH{i:05d}" for i in range(1, n + 1)],
        "tuoi": tuoi, "goi_cuoc": goi, "khu_vuc": khu_vuc,
        "so_thang_su_dung": so_thang, "cuoc_hang_thang": cuoc_hang_thang,
        "tong_cuoc": np.round(so_thang * cuoc_hang_thang, 0),
        "so_lan_goi_ho_tro": so_lan_goi.astype(float), "label": label,
    })
    # mot it gia tri thieu de Imputer co viec lam
    for c in ["tuoi", "cuoc_hang_thang"]:
        idx = rng.choice(n, size=int(0.02 * n), replace=False); df.loc[idx, c] = np.nan
    df.to_csv(out("churn.csv"), index=False)
    df.dropna().to_parquet(out("churn.parquet"), index=False)
    # khach hang moi (chua biet nhan) cho buoc du doan theo lo
    moi = df.sample(500, random_state=SEED).copy()
    moi["ma_kh"] = [f"KM{i:05d}" for i in range(1, 501)]
    moi["label"] = np.nan
    moi.to_csv(out("churn_moi.csv"), index=False)
    print("Ty le roi bo:", round(label.mean(), 3))


def gen_house_prices(n=6000):
    dien_tich = np.round(rng.lognormal(np.log(75), 0.4, n), 1)
    so_phong_ngu = np.clip((dien_tich / 30).round() + rng.integers(-1, 2, n), 1, 6).astype(int)
    so_phong_tam = np.clip(so_phong_ngu - rng.integers(0, 2, n), 1, 4).astype(int)
    khoang_cach = np.round(rng.gamma(2.2, 3.5, n), 1)
    tuoi_nha = rng.integers(0, 40, n).astype(float)
    gia = (dien_tich * 25 + so_phong_ngu * 180 + so_phong_tam * 120 - khoang_cach * 95 - tuoi_nha * 22
           + 800 + rng.normal(0, 350, n))
    df = pd.DataFrame({"dien_tich": dien_tich, "so_phong_ngu": so_phong_ngu, "so_phong_tam": so_phong_tam,
                       "khoang_cach_trung_tam": khoang_cach, "tuoi_nha": tuoi_nha,
                       "gia_nha": np.round(np.clip(gia, 300, None), 0)})
    df.to_parquet(out("house_prices.parquet"), index=False)


if __name__ == "__main__":
    gen_vanban(); gen_access_log(); gen_giaodich(); gen_diem_thi(); gen_donhang(); gen_don_hang_rfm()
    gen_khach_hang(); gen_churn(); gen_house_prices()
    print("Da sinh du lieu vao", HERE)
