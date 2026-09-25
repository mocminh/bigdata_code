# Giáo trình Dữ liệu lớn — Mã nguồn và dữ liệu thực hành

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PySpark 3.5.7](https://img.shields.io/badge/PySpark-3.5.7-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org/docs/3.5.7/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch01/ch01.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Kho mã nguồn chính thức đi kèm **Giáo trình Dữ liệu lớn** — Huỳnh Đệ Thủ (chủ biên), Hồ Nhựt Minh; Trường Đại học Quốc tế Sài Gòn (SIU), 2026.
Kho cung cấp toàn bộ **75 đoạn mã** in trong sách, **8 notebook** thực hành theo chương chạy trực tiếp trên Google Colab,
các **tập dữ liệu mẫu** tái lập được và **môi trường phần mềm tham chiếu** (Bảng 2.3 của giáo trình).

> *Companion code for the textbook **Dữ liệu lớn** (Big Data), Saigon International University, 2026 — all 75 code listings,
> per-chapter Google Colab notebooks, reproducible sample datasets and the pinned reference environment (PySpark 3.5.7).*

## Nội dung theo chương

| Chương | Tên chương | Đoạn mã | Notebook |
|:-:|---|:-:|:-:|
| 1 | Tổng quan về dữ liệu lớn | 1.1 – 1.2 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch01/ch01.ipynb) |
| 2 | Thiết lập môi trường PySpark | 2.1 – 2.7 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch02/ch02.ipynb) |
| 3 | RDD – cấu trúc dữ liệu phân tán | 3.1 – 3.12 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch03/ch03.ipynb) |
| 4 | DataFrame và Spark SQL | 4.1 – 4.15 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch04/ch04.ipynb) |
| 5 | Tiền xử lý và đặc trưng hóa trên dữ liệu lớn | 5.1 – 5.19 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch05/ch05.ipynb) |
| 6 | Học máy có giám sát trên dữ liệu lớn | 6.1 – 6.9 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch06/ch06.ipynb) |
| 7 | Học máy không giám sát trên dữ liệu lớn | 7.1 – 7.6 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch07/ch07.ipynb) |
| 8 | Học sâu trên dữ liệu lớn *(mở rộng, cần GPU)* | 8.1 – 8.5 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch08/ch08.ipynb) |

Mỗi đoạn mã còn được lưu **nguyên văn như trong sách** tại `code/chXX/doan_ma_<chương>_<số>.py` (ví dụ `code/ch06/doan_ma_6_9.py`).

## Bắt đầu nhanh

### Google Colab (khuyến nghị cho người học)

Nhấn nút *Open in Colab* của chương cần học. Ô lệnh đầu tiên của mỗi notebook cài PySpark 3.5.7 và tải kho mã về máy ảo:

```python
!pip install -q pyspark==3.5.7 pyarrow==16.1.0 pandas==2.2.2
!git clone -q https://github.com/mocminh/bigdata_code
%cd bigdata_code
```

### Máy cá nhân

```bash
git clone https://github.com/mocminh/bigdata_code.git
cd bigdata_code
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -c "import pyspark; print(pyspark.__version__)"  # 3.5.7
```

Cần **OpenJDK 11 hoặc 17** (`java -version`). Với JDK 21, các đoạn mã dùng Apache Arrow / pandas UDF không chạy được.
Môi trường conda tương đương: `conda env create -f environment.yml`.

### Databricks Free Edition

- Đối tượng `spark` đã có sẵn; cài thư viện bằng `%pip install -r requirements.txt` ở đầu notebook.
- Tải thư mục `data/` lên một volume của Unity Catalog và thay đường dẫn bằng
  `/Volumes/<catalog>/<schema>/<volume>/<tệp>` (Mục 2.2.2 của giáo trình).

## Cấu trúc kho

```
bigdata_code/
├── code/
│   ├── ch01/ … ch08/          # mỗi chương một thư mục
│   │   ├── doan_ma_<c>_<n>.py # đoạn mã <c>.<n> nguyên văn như trong sách (đường dẫn HDFS/Volume)
│   │   └── ch0<c>.ipynb       # notebook tổng hợp của chương (đường dẫn cục bộ, ô chuẩn bị, chạy trên Colab)
│   └── ch02/tien_ich.zip      # mô-đun mẫu cho Đoạn mã 2.5 (--py-files / addPyFile)
├── data/                      # tập dữ liệu mẫu (xem data/README.md), sinh lại bằng data/generate_data.py
│   └── movielens/             # hướng dẫn và script tải MovieLens ml-latest-small (Đoạn mã 7.4)
├── tests/
│   ├── run_listings.py        # chạy tuần tự mọi đoạn mã trên Spark local
│   ├── listings.json          # danh mục đoạn mã dùng cho run_listings.py
│   └── report.md              # kết quả chạy trên môi trường tham chiếu
├── requirements.txt           # thư viện đã ghim phiên bản cho Chương 1–7 (Bảng 2.3)
├── requirements-ch08.txt      # thư viện học sâu cho Chương 8 (cần GPU)
├── environment.yml            # môi trường conda để đóng gói bằng conda-pack (Mục 2.4.3)
├── CITATION.cff               # thông tin trích dẫn
└── LICENSE
```

## Môi trường tham chiếu (Bảng 2.3)

| Thành phần | Phiên bản |
|---|---|
| Python | 3.11 (tương thích 3.10 – 3.12) |
| Java | OpenJDK 17 (hoặc 11) |
| Apache Spark / PySpark | 3.5.7 |
| pandas / NumPy / PyArrow | 2.2.2 / 1.26.4 / 16.1.0 |
| Matplotlib | 3.9.2 |
| MLflow | 2.17.2 |
| TensorFlow / PyTorch | 2.15.1 / 2.4.1 |
| Horovod / Petastorm | 0.28.1 / 0.12.1 |

## Dữ liệu mẫu

Toàn bộ dữ liệu trong `data/` là dữ liệu **mô phỏng** sinh bằng `data/generate_data.py` với hạt giống cố định (seed 2026),
nên có thể tái lập nguyên vẹn; lược đồ từng tệp được mô tả trong [`data/README.md`](data/README.md).
Riêng bộ **MovieLens ml-latest-small** (Đoạn mã 7.4) không được phân phối lại theo giấy phép của GroupLens — tải về bằng
`python data/movielens/download_movielens.py` (ô chuẩn bị trong `ch07.ipynb` tự thực hiện việc này).

## Quy ước đường dẫn

Các đoạn mã trong sách dùng đường dẫn HDFS để nhấn mạnh bối cảnh cụm máy; notebook trong kho đã đổi sang đường dẫn cục bộ.

| Trong sách | Google Colab / máy cá nhân | Databricks Free Edition |
|---|---|---|
| `hdfs:///data/<tệp>`, `hdfs://namenode:9000/data/<tệp>` | `data/<tệp>` | `/Volumes/<catalog>/<schema>/<volume>/<tệp>` |
| `hdfs:///models/…`, `hdfs://namenode:9000/models/…` | `models/…` | volume ghi được của workspace |
| `hdfs:///output/…`, `hdfs://namenode:9000/ketqua/…`, `hdfs:///warehouse/…` | `output/…` | volume ghi được của workspace |
| `/mnt/models/…`, `/mnt/ckpt/…` (Chương 8) | `models/…` | volume ghi được của workspace |

## Tái lập kết quả

```bash
python data/generate_data.py                 # sinh lại dữ liệu mẫu (tùy chọn)
python data/movielens/download_movielens.py  # tải MovieLens cho Đoạn mã 7.4
python tests/run_listings.py                 # chạy tất cả chương; hoặc: python tests/run_listings.py 6 7
```

`tests/run_listings.py` chạy lần lượt mọi đoạn mã trên một phiên Spark cục bộ và ghi kết quả vào
[`tests/report.md`](tests/report.md). Trên môi trường tham chiếu (PySpark 3.5.7, OpenJDK 17, Python 3.11),
**67 đoạn mã chạy trực tiếp**; 8 đoạn mã còn lại là lệnh shell (2.4, 2.6), ví dụ minh họa một lỗi phương pháp (5.19)
hoặc cần GPU cùng TensorFlow / Horovod / MLflow (8.1 – 8.5). Các khung bài tập (3.12, 5.16, 5.18, 7.5) chạy được
nhờ ô "chuẩn bị" đặt ngay trước đoạn mã trong notebook.

Mã nguồn khớp với bản in của giáo trình (2026) và dùng API PySpark 3.5.

## Chương 8 (học sâu)

Các đoạn mã Chương 8 cần GPU và các thư viện trong `requirements-ch08.txt`
(TensorFlow 2.15.1 – Keras 2 để tương thích Horovod 0.28.1; PyTorch 2.4.1; MLflow 2.17.2).
Với TensorFlow ≥ 2.16 (Keras 3) hãy cài thêm `tf-keras` và đặt `TF_USE_LEGACY_KERAS=1`.
Dự án Horovod đã được lưu trữ (archived) vào tháng 9/2026 và 0.28.1 là phiên bản cuối: thư viện vẫn cài và chạy được
với môi trường trên, nhưng với dự án mới nên ưu tiên TorchDistributor (Đoạn mã 8.2) hoặc `tf.distribute`.
Notebook `ch08.ipynb` dùng để đọc và chỉnh sửa mã, không chạy trực tiếp trên Colab miễn phí.

## Báo lỗi và góp ý

Phát hiện lỗi trong mã nguồn hoặc điểm chưa khớp với sách, vui lòng mở một
[issue](https://github.com/mocminh/bigdata_code/issues) ghi rõ số hiệu đoạn mã, môi trường chạy và thông báo lỗi.

## Trích dẫn

Huỳnh Đệ Thủ, Hồ Nhựt Minh (2026). *Giáo trình Dữ liệu lớn*. Trường Đại học Quốc tế Sài Gòn. Mã nguồn: https://github.com/mocminh/bigdata_code

Thông tin trích dẫn ở dạng máy đọc được nằm trong [`CITATION.cff`](CITATION.cff).

## Giấy phép

Mã nguồn và dữ liệu mô phỏng trong kho được phát hành theo giấy phép [MIT](LICENSE).
Bộ dữ liệu MovieLens thuộc GroupLens Research (Đại học Minnesota) và tuân theo điều khoản sử dụng riêng của GroupLens.
