# MovieLens (ml-latest-small)

Đoạn mã 7.4 dùng tệp `ratings.csv` (cột `userId`, `movieId`, `rating`, `timestamp`) của bộ dữ liệu
**MovieLens ml-latest-small** do GroupLens Research (Đại học Minnesota) công bố. Kho mã không kèm tệp này; người học
tải về bằng:

```bash
python data/movielens/download_movielens.py
```

hoặc ô "chuẩn bị" trong `code/ch07/ch07.ipynb` sẽ tự tải khi thiếu tệp.

Dữ liệu được sử dụng theo điều khoản sử dụng của GroupLens (mục *Usage License* trong
[tệp mô tả của bộ dữ liệu](https://files.grouplens.org/datasets/movielens/ml-latest-small-README.html)), trong đó có các
điều kiện: không dùng cho mục đích thương mại khi chưa được GroupLens cho phép, không ngụ ý được Đại học Minnesota hay
GroupLens bảo trợ, và ghi nhận việc sử dụng bộ dữ liệu trong các công bố bằng cách trích dẫn:

F. M. Harper, J. A. Konstan, "The MovieLens Datasets: History and Context",
*ACM Transactions on Interactive Intelligent Systems*, 5(4), bài 19, tr. 19:1 – 19:19, 2015.
https://doi.org/10.1145/2827872 — trang bộ dữ liệu: https://grouplens.org/datasets/movielens/
