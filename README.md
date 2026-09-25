# Giáo trình Dữ liệu lớn — Mã nguồn và dữ liệu thực hành

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PySpark 3.5.7](https://img.shields.io/badge/PySpark-3.5.7-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org/docs/3.5.7/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mocminh/bigdata_code/blob/main/code/ch01/ch01.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Kho mã nguồn chính thức đi kèm **Giáo trình Dữ liệu lớn** — Huỳnh Đệ Thủ (chủ biên), Hồ Nhựt Minh; Trường Đại học Quốc tế Sài Gòn (SIU), 2026.
Kho cung cấp toàn bộ **75 đoạn mã** in trong sách, **8 notebook** thực hành theo chương (notebook Chương 1 – 7 chạy trực tiếp
trên Google Colab; notebook Chương 8 cần GPU), các **tập dữ liệu mẫu** tái lập được và **môi trường phần mềm tham chiếu**
(Bảng 2.3 của giáo trình).

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

Nhấn nút *Open in Colab* của chương cần học. Ô lệnh đầu tiên của mỗi notebook cài OpenJDK 17 và PySpark 3.5.7
(như Đoạn mã 2.1) rồi tải kho mã về máy ảo:

```python
# Buoc 1: cai OpenJDK 17 (Spark 3.5 ho tro Java 8/11/17)
!apt-get update -qq
!apt-get install -y -qq openjdk-17-jdk-headless > /dev/null
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"
# Buoc 2: cai dat PySpark tu PyPI (ghim phien ban theo Bang 2.3)
!pip install -q pyspark==3.5.7
!git clone -q https://github.com/mocminh/bigdata_code
%cd bigdata_code
```

Runtime mặc định của Colab (9/2026) là máy ảo Ubuntu 24.04 với Python 3.13 và chỉ cài sẵn OpenJDK 21, trong khi Spark 3.5
hỗ trợ Java 8/11/17 (với Java 21, các thao tác dùng Apache Arrow như `toPandas()` hay pandas UDF bị lỗi). Vì vậy ô cài đặt
cài thêm OpenJDK 17 và đặt `JAVA_HOME` trước khi khởi tạo SparkSession, chỉ ghim `pyspark==3.5.7` và giữ nguyên pandas,
pyarrow có sẵn của Colab: pyarrow 16.1.0 và pandas 2.2.2 (Bảng 2.3) chỉ có bản dựng sẵn cho Python 3.12 trở xuống nên
không cài được trên Python 3.13 (không dùng `requirements.txt` trên Colab). Mỗi lần Colab cấp máy ảo mới, phần mềm đã cài
bị mất, nên cần chạy lại ô cài đặt ở đầu mỗi phiên. Kết quả chạy thử trên môi trường tương đương runtime Colab 9/2026:
[`tests/report_colab.md`](tests/report_colab.md). Notebook `ch08.ipynb` cần GPU, chỉ dùng để đọc và chỉnh sửa mã.

### Máy cá nhân

```bash
git clone https://github.com/mocminh/bigdata_code.git
cd bigdata_code
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -c "import pyspark; print(pyspark.__version__)"  # 3.5.7
```

Cần **OpenJDK 17 (hoặc 11)** (`java -version`): Spark 3.5 hỗ trợ Java 8/11/17, với JDK 21 các đoạn mã dùng Apache Arrow /
pandas UDF không chạy được. Các phiên bản trong `requirements.txt` được ghim cho Python 3.11 (Bảng 2.3) và cài được trên
Python 3.10 – 3.12; từ Python 3.12 cần thêm gói `setuptools` (`pip install setuptools`) vì PySpark 3.5 còn dùng mô-đun
`distutils` đã bị gỡ khỏi thư viện chuẩn. Chương 1 – 7 chạy được với Python 3.10 – 3.13; với Python 3.13, dùng bộ phiên bản
đã chạy thử trong [`tests/report_colab.md`](tests/report_colab.md) thay cho `requirements.txt`:
`pip install pyspark==3.5.7 pandas==2.2.3 numpy==2.1.3 pyarrow==23.0.1 matplotlib==3.10.0 setuptools`.
Môi trường conda tương đương: `conda env create -f environment.yml`.

### Databricks Free Edition

- Free Edition chỉ có **tính toán serverless** (chạy qua Spark Connect): đối tượng `spark` đã có sẵn, Spark và Java
  do nền tảng cung cấp, nên bỏ ô cài đặt ở đầu mỗi notebook (không cài `pyspark`).
- Tính toán serverless chỉ hỗ trợ API DataFrame và Spark SQL: không hỗ trợ API RDD/`SparkContext`
  (Đoạn mã 1.1, 1.2, 2.5, 3.1 – 3.9, 3.12, 4.3), `cache()`/`persist()` (Đoạn mã 3.6, 6.9) và Spark UI; các đoạn mã này
  chạy trên Google Colab hoặc máy cá nhân. Free Edition dùng cho các đoạn mã API DataFrame của Chương 2, 4 – 7 (Bảng 2.3).
- Thư viện bổ sung được khai báo trong bảng **Environment** của notebook (hoặc cài bằng `%pip install` ở đầu notebook).
- Dữ liệu đặt trong volume `/Volumes/workspace/default/du_lieu/` do người học tự tạo
  (ví dụ `CREATE VOLUME IF NOT EXISTS workspace.default.du_lieu`): tải các tệp trong `data/` lên volume này và thay
  `data/` bằng `/Volumes/workspace/default/du_lieu/` (Mục 2.2.2 của giáo trình).

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
│   ├── report.md              # kết quả chạy trên môi trường tham chiếu
│   └── report_colab.md        # kết quả chạy trên môi trường tương đương runtime Colab 9/2026
├── requirements.txt           # thư viện đã ghim phiên bản cho Chương 1–7 (Bảng 2.3, Python 3.11)
├── requirements-ch08.txt      # thư viện học sâu cho Chương 8 (cần GPU)
├── environment.yml            # môi trường conda để đóng gói bằng conda-pack (Mục 2.4.3)
├── CITATION.cff               # thông tin trích dẫn
└── LICENSE
```

## Môi trường tham chiếu (Bảng 2.3)

| Thành phần | Phiên bản | Ghi chú |
|---|---|---|
| Python | 3.11 | Chương 1 – 7 chạy được với Python 3.10 – 3.13 (từ 3.12 cần gói `setuptools`); TensorFlow 2.15.1 của Chương 8 chỉ hỗ trợ Python 3.9 – 3.11 |
| Java | OpenJDK 17 (hoặc 11) | Spark 3.5 hỗ trợ Java 8/11/17; runtime Colab 9/2026 chỉ có OpenJDK 21 nên phải cài thêm OpenJDK 17 (Đoạn mã 2.1) |
| Apache Spark / PySpark | 3.5.7 | `pip install pyspark==3.5.7`, kèm Py4J 0.10.9.7 |
| pandas / NumPy / PyArrow | 2.2.2 / 1.26.4 / 16.1.0 | Trên Colab dùng bản cài sẵn của runtime |
| Matplotlib | 3.9.2 | Chương 5, 7 |
| MLflow | 2.17.2 | Chương 8 dùng bí danh (alias) của Model Registry, chạy được trên dòng 2.x, 3.x và trên Unity Catalog |
| TensorFlow (Keras 2) / PyTorch | 2.15.1 / 2.4.1 | Chương 8, cần GPU |
| Horovod / Petastorm | 0.28.1 / 0.12.1 | Horovod đã lưu trữ (archived) từ 9/2026, 0.28.1 là phiên bản cuối |

Bảng 2.3 ghi phiên bản theo dòng (ví dụ pandas 2.2.x, PyArrow 16.x); phiên bản cụ thể được ghim trong `requirements.txt`
(Chương 1 – 7) và `requirements-ch08.txt` (Chương 8). Khi có khác biệt, các tệp này là nguồn tham chiếu cuối cùng.

## Dữ liệu mẫu

Toàn bộ dữ liệu trong `data/` là dữ liệu **mô phỏng** sinh bằng `data/generate_data.py` với hạt giống cố định (seed 2026),
nên có thể tái lập nguyên vẹn; lược đồ từng tệp được mô tả trong [`data/README.md`](data/README.md).
Riêng bộ **MovieLens ml-latest-small** của GroupLens (Đoạn mã 7.4) không kèm trong kho: người học tải về bằng
`python data/movielens/download_movielens.py` (ô chuẩn bị trong `ch07.ipynb` tự thực hiện việc này), sử dụng dữ liệu theo
điều khoản sử dụng của GroupLens và trích dẫn Harper & Konstan (2015) khi công bố kết quả có dùng bộ dữ liệu này
(xem [`data/movielens/README.md`](data/movielens/README.md)).

## Quy ước đường dẫn

Các đoạn mã trong sách dùng đường dẫn HDFS để nhấn mạnh bối cảnh cụm máy; notebook trong kho đã đổi sang đường dẫn cục bộ.
Trên Databricks Free Edition, đường dẫn volume có dạng `/Volumes/<catalog>/<schema>/<volume>/`; bảng dưới dùng volume
`du_lieu` trong schema `default` của catalog `workspace` như ví dụ ở Mục 2.2.2.

| Trong sách | Google Colab / máy cá nhân | Databricks Free Edition |
|---|---|---|
| `hdfs:///data/<tệp>`, `hdfs://namenode:9000/data/<tệp>` | `data/<tệp>` | `/Volumes/workspace/default/du_lieu/<tệp>` |
| `/Volumes/workspace/default/du_lieu/<tệp>` (Đoạn mã 2.2), `diem_thi.csv` (Đoạn mã 2.3), `file:///opt/spark/data/<tệp>` (Đoạn mã 3.1) | `data/<tệp>` | `/Volumes/workspace/default/du_lieu/<tệp>` |
| `hdfs:///models/…`, `hdfs://namenode:9000/models/…` | `models/…` | volume ghi được của workspace |
| `hdfs:///output/…`, `hdfs://namenode:9000/ketqua/…`, `hdfs:///warehouse/…`, `/data/ketqua_du_doan` (Đoạn mã 8.5) | `output/…` | volume ghi được của workspace |
| `/mnt/models/…`, `/mnt/ckpt/…` (Chương 8) | `models/…` | volume ghi được của workspace |
| tên thí nghiệm MLflow `/exp/image-classifier` (Đoạn mã 8.4) | `image-classifier` | đường dẫn tuyệt đối trong workspace, ví dụ `/Users/<email>/image-classifier` |

## Tái lập kết quả

```bash
python data/generate_data.py                 # sinh lại dữ liệu mẫu (tùy chọn)
python data/movielens/download_movielens.py  # tải MovieLens cho Đoạn mã 7.4
python tests/run_listings.py                 # chạy tất cả chương; hoặc: python tests/run_listings.py 6 7
```

`tests/run_listings.py` chạy lần lượt mọi đoạn mã (bản đường dẫn cục bộ như trong notebook, bỏ qua các dòng lệnh shell
bắt đầu bằng `!`) trên một phiên Spark cục bộ và ghi kết quả vào [`tests/report.md`](tests/report.md).
Trên môi trường tham chiếu (PySpark 3.5.7, OpenJDK 17, Python 3.11), **67 đoạn mã chạy trực tiếp**; 8 đoạn mã còn lại
là lệnh shell (2.4, 2.6), ví dụ minh họa một lỗi phương pháp (5.19) hoặc cần GPU cùng TensorFlow / PyTorch / Horovod /
MLflow (8.1 – 8.5). Các đoạn mã cần tệp, biến hoặc hàm mà sách giả định đã có (ví dụ khung bài tập 3.12, 7.5) chạy được
nhờ ô "chuẩn bị" đặt ngay trước đoạn mã trong notebook (Đoạn mã 2.5, 3.12, 5.10, 5.11, 5.15, 5.16, 7.1, 7.4, 7.5);
nội dung các ô này cũng nằm trong trường `prep` của `tests/listings.json`.

Kết quả chạy cùng tập lệnh trên môi trường tương đương runtime Google Colab 9/2026 (Python 3.13, OpenJDK 17,
PySpark 3.5.7 cùng pandas và pyarrow bản cài sẵn của Colab) được lưu riêng tại
[`tests/report_colab.md`](tests/report_colab.md): 66 đoạn mã chạy được, không có lỗi; Đoạn mã 7.4 chưa chạy được
trong môi trường kiểm thử vì không truy cập được files.grouplens.org để tải dữ liệu MovieLens (không phải lỗi mã).

Mã nguồn khớp với bản in của giáo trình (2026) và dùng API PySpark 3.5.

## Chương 8 (học sâu)

Các đoạn mã Chương 8 cần GPU, mô hình và dữ liệu của người học cùng các thư viện trong `requirements-ch08.txt`
(TensorFlow 2.15.1 với Keras 2, PyTorch 2.4.1, MLflow 2.17.2, Horovod 0.28.1, Petastorm 0.12.1), cài sau
`requirements.txt` trên Python 3.11 (TensorFlow 2.15.1 chỉ hỗ trợ Python 3.9 – 3.11). Với TensorFlow 2.16 trở lên
(Keras 3), cài thêm `tf-keras` và đặt `TF_USE_LEGACY_KERAS=1` để giữ Keras 2. TorchDistributor (Đoạn mã 8.2) yêu cầu
Spark 3.4 trở lên. Notebook `ch08.ipynb` dùng để đọc và chỉnh sửa mã, không chạy trực tiếp trên Colab miễn phí.

**Horovod (Đoạn mã 8.3).** Dự án Horovod đã ngừng phát triển: phiên bản cuối là 0.28.1 (phát hành 6/2023) và kho mã
được chuyển sang trạng thái lưu trữ (archived) từ tháng 9/2026. Tài liệu chính thức của Horovod chỉ ghi nhận tương thích
tới TensorFlow 2.12, nên cần tự kiểm thử trước khi dùng với môi trường đã ghim (TensorFlow 2.15.1); việc cài đặt trên máy
GPU cần trình biên dịch C++ và NCCL hoặc MPI. Với dự án mới, nên ưu tiên các công cụ hiện hành dùng cùng cơ chế
All-Reduce: TorchDistributor (Đoạn mã 8.2) hoặc `tf.distribute.MultiWorkerMirroredStrategy`.

**MLflow (Đoạn mã 8.4).** Mã đăng ký mô hình vào Model Registry, gán bí danh (alias) `champion` cho phiên bản đã kiểm định
và nạp mô hình theo URI `models:/cnn_classifier@champion`. Bí danh có từ MLflow 2.3 và chạy được trên dòng 2.x, 3.x cũng
như trên Unity Catalog. Cách cũ dùng các giai đoạn Staging/Production (URI dạng `models:/cnn_classifier/Production`) đã bị
đánh dấu lỗi thời từ MLflow 2.9 và không được Model Registry trong Unity Catalog của Databricks (kể cả Free Edition) hỗ trợ;
trên Unity Catalog, tên mô hình có dạng ba cấp `<catalog>.<schema>.<model>`, ví dụ
`models:/<catalog>.<schema>.cnn_classifier@champion`. Khi tự triển khai MLflow với cơ sở dữ liệu lưu metadata (sqlite,
PostgreSQL…), MLflow 2.17.2 cần SQLAlchemy dòng 2.0 (đã ghim trong `requirements-ch08.txt`), vì không tương thích với
SQLAlchemy 2.1.

## Báo lỗi và góp ý

Phát hiện lỗi trong mã nguồn hoặc điểm chưa khớp với sách, vui lòng mở một
[issue](https://github.com/mocminh/bigdata_code/issues) ghi rõ số hiệu đoạn mã, môi trường chạy và thông báo lỗi.

## Trích dẫn

Huỳnh Đệ Thủ, Hồ Nhựt Minh (2026). *Giáo trình Dữ liệu lớn*. Trường Đại học Quốc tế Sài Gòn. Mã nguồn: https://github.com/mocminh/bigdata_code

Thông tin trích dẫn ở dạng máy đọc được nằm trong [`CITATION.cff`](CITATION.cff).

Khi công bố kết quả có dùng bộ dữ liệu MovieLens (Đoạn mã 7.4), trích dẫn thêm: F. M. Harper, J. A. Konstan,
"The MovieLens Datasets: History and Context", *ACM Transactions on Interactive Intelligent Systems*, 5(4), bài 19,
tr. 19:1 – 19:19, 2015. https://doi.org/10.1145/2827872

## Giấy phép

Mã nguồn và dữ liệu mô phỏng trong kho được phát hành theo giấy phép [MIT](LICENSE).
Bộ dữ liệu MovieLens thuộc GroupLens Research (Đại học Minnesota), không kèm trong kho và được sử dụng theo điều khoản
sử dụng riêng của GroupLens.
