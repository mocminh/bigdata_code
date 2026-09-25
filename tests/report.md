# Kết quả chạy các đoạn mã trên môi trường tham chiếu (67 chạy được, 0 lỗi, 8 bỏ qua)

Môi trường: PySpark 3.5.7, OpenJDK 17 (Temurin), Python 3.11, Spark local[2]; chạy bằng `python tests/run_listings.py`. Đoạn mã 7.4 cần tệp `data/movielens/ratings.csv` tải bằng `data/movielens/download_movielens.py`.

| Đoạn mã | Tên | Kết quả | Ghi chú | Thời gian (s) |
|---|---|---|---|---|
| Đoạn mã 1.1 | Chương trình đếm từ bằng PySpark. | ĐẠT | bo 1 | 5.1 |
| Đoạn mã 1.2 | Chuỗi phép biến đổi thống kê lỗi theo địa chỉ IP. | ĐẠT |  | 1.0 |
| Đoạn mã 2.1 | Cài đặt và khởi tạo PySpark trên Google Colab. | ĐẠT | Ket qua dem: 9999999 | 5.0 |
| Đoạn mã 2.2 | Đọc tệp CSV đã tải lên volume trong notebook Databricks. | ĐẠT | only showing top 5 rows | 2.2 |
| Đoạn mã 2.3 | Ứng dụng PySpark hoàn chỉnh: đọc CSV, thống kê và dừng phiên. | ĐẠT | only showing top 10 rows | 3.4 |
| Đoạn mã 2.4 | Nộp ứng dụng lên cụm YARN bằng spark-submit. | BỎ QUA | lệnh shell spark-submit (chạy trên terminal, cần cụm YARN) | 0.0 |
| Đoạn mã 2.5 | Phân phối mã nguồn dùng chung cho các executor. | ĐẠT | da sao chep tien_ich.zip | 0.3 |
| Đoạn mã 2.6 | Đóng gói môi trường conda và nộp lên cụm YARN. | BỎ QUA | lệnh shell conda-pack (chỉ minh họa) | 0.0 |
| Đoạn mã 2.7 | Cài đặt theo phiên bản đã ghim và kiểm tra môi trường thực hành. | ĐẠT | pyarrow: 16.1.0 | 8.2 |
| Đoạn mã 3.1 | Khởi tạo SparkContext và tạo RDD bằng parallelize, textFile. | ĐẠT | [7.5, 8.0, 6.5] | 1.5 |
| Đoạn mã 3.2 | Kiểm tra và điều chỉnh số partition của RDD. | ĐẠT | 16 4 | 0.0 |
| Đoạn mã 3.3 | Các phép biến đổi cơ bản trên RDD. | ĐẠT | [7, 7, 7] | 1.0 |
| Đoạn mã 3.4 | Chuỗi biến đổi chỉ được thực thi khi gặp action. | ĐẠT |  /  data/access.log HadoopRDD[25] at textFile at NativeMethodAccessorImpl.java:0 | 1.1 |
| Đoạn mã 3.5 | Các action thông dụng trên RDD. | ĐẠT | Diem trung binh: 7.5 | 4.1 |
| Đoạn mã 3.6 | Đo khác biệt thời gian trước và sau khi cache RDD. | ĐẠT | Da cache:   0.34 giay | 1.7 |
| Đoạn mã 3.7 | So sánh groupByKey và reduceByKey trên cùng bài toán. | ĐẠT | True | 1.3 |
| Đoạn mã 3.8 | Chương trình đếm từ hoàn chỉnh với RDD. | ĐẠT | tan             1 | 2.7 |
| Đoạn mã 3.9 | Kết nối hai tập dữ liệu sinh viên và điểm thi. | ĐẠT | {'SV01': 2, 'SV02': 1, 'SV05': 1} | 5.5 |
| Đoạn mã 3.10 | Dữ liệu mẫu cho bài tập đếm từ. | ĐẠT |  | 0.0 |
| Đoạn mã 3.11 | Dữ liệu mẫu cho bài tập Pair RDD. | ĐẠT |  | 0.0 |
| Đoạn mã 3.12 | Hai nhánh phân tích dùng chung một RDD trung gian. | ĐẠT |  | 1.3 |
| Đoạn mã 4.1 | Tạo DataFrame từ tập hợp cục bộ bằng createDataFrame. | ĐẠT |  /-- tuoi: integer (nullable = true) | 3.6 |
| Đoạn mã 4.2 | Đọc DataFrame từ các tệp CSV, JSON và Parquet. | ĐẠT |  | 1.9 |
| Đoạn mã 4.3 | Tạo DataFrame từ RDD với lược đồ StructType tường minh. | ĐẠT |  /-- gia: double (nullable = true) | 0.1 |
| Đoạn mã 4.4 | Xem kế hoạch truy vấn bằng explain(). | ĐẠT |       +- FileScan parquet [ma_don#394,don_gia#399,khu_vuc#401] Batched: true, Da | 0.3 |
| Đoạn mã 4.5 | Khởi tạo tập dữ liệu bán hàng dùng chung cho cả chương. | ĐẠT | +------+-----+----------+----------+--------+-------+----------+-------+ | 0.9 |
| Đoạn mã 4.6 | Các thao tác select, withColumn, filter/where và orderBy. | ĐẠT | only showing top 5 rows | 2.2 |
| Đoạn mã 4.7 | Tổng hợp doanh thu theo danh mục với groupBy và agg. | ĐẠT | +----------+------+--------------+------------+-------------+------------+ | 0.9 |
| Đoạn mã 4.8 | Xử lý giá trị thiếu bằng dropna và fillna. | ĐẠT |  | 0.1 |
| Đoạn mã 4.9 | Các loại join giữa bảng đơn hàng và bảng khách hàng. | ĐẠT | +-----+------+----------+----------+--------+-------+----------+-------+-------- | 4.6 |
| Đoạn mã 4.10 | Đăng ký khung nhìn tạm và truy vấn bằng spark.sql. | ĐẠT | +--------+------+--------------+------------+ | 1.0 |
| Đoạn mã 4.11 | Khung nhìn tạm toàn cục và truy vấn join bằng SQL. | ĐẠT | +------+-------------+----------+----------+ | 1.2 |
| Đoạn mã 4.12 | Ghi và đọc lại bảng Parquet có phân vùng theo khu vực. | ĐẠT | +------+-----+----------+----------+--------+-------+----------+----------+----- | 1.8 |
| Đoạn mã 4.13 | Định nghĩa và đăng ký UDF cho DataFrame API và cho SQL. | ĐẠT | +------+----------+----------+ | 2.8 |
| Đoạn mã 4.14 | Pandas UDF vector hóa trao đổi dữ liệu qua Apache Arrow. | ĐẠT | +------+-----+----------+----------+--------+-------+----------+-------+-------- | 3.0 |
| Đoạn mã 4.15 | Thay thế UDF bằng hàm dựng sẵn when/otherwise. | ĐẠT | +------+-----+----------+----------+--------+-------+----------+-------+-------- | 0.5 |
| Đoạn mã 5.1 | Thống kê mô tả với describe và summary. | ĐẠT | +-------+------------------+-----------------+ | 1.9 |
| Đoạn mã 5.2 | Đếm số giá trị null trên từng cột trong một lần quét. | ĐẠT | +-----+----+--------+--------+-----------+---------+-----------+-------------+ | 0.9 |
| Đoạn mã 5.3 | Phân phối tần suất, phân vị xấp xỉ và tương quan. | ĐẠT | Tuong quan thu nhap - chi tieu: 0.14354283229192166 | 0.9 |
| Đoạn mã 5.4 | Lấy mẫu và chuyển sang pandas để trực quan hóa. | ĐẠT | Kich thuoc mau: 221 | 3.7 |
| Đoạn mã 5.5 | Phát hiện lệch phân phối và biến đổi logarit. | ĐẠT | Trung binh: 22.28446987268679 - Trung vi: 17.2 | 1.0 |
| Đoạn mã 5.6 | Xóa dòng thiếu với dropna: how, thresh và subset. | ĐẠT | Truoc: 20000 - Sau khi loc: 19011 | 0.4 |
| Đoạn mã 5.7 | Điền khuyết bằng fillna và Imputer với trung vị. | ĐẠT | +----+--------+ | 1.0 |
| Đoạn mã 5.8 | Lọc ngoại lai theo quy tắc IQR với approxQuantile. | ĐẠT | So quan sat bi loai: 1336 | 0.8 |
| Đoạn mã 5.9 | Winsorize giá trị vượt ngưỡng bằng when/otherwise. | ĐẠT | +-------+-----------------+------------------+ | 0.6 |
| Đoạn mã 5.10 | StringIndexer và IndexToString trên cột nghề nghiệp. | ĐẠT | ('nhan_vien', 'ky_su', 'kinh_doanh', 'giao_vien', 'sinh_vien', 'bac_si') | 2.0 |
| Đoạn mã 5.11 | OneHotEncoder cho hai cột nghề nghiệp và thành phố. | ĐẠT | only showing top 5 rows | 1.5 |
| Đoạn mã 5.12 | VectorAssembler gom các cột thành vector features. | ĐẠT | only showing top 3 rows | 0.5 |
| Đoạn mã 5.13 | Chuỗi assembler và scaler, fit trên train rồi transform test. | ĐẠT |  | 2.5 |
| Đoạn mã 5.14 | MinMaxScaler và RobustScaler trên cùng cột vector. | ĐẠT |  | 2.2 |
| Đoạn mã 5.15 | Pipeline hoàn chỉnh: StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler. | ĐẠT | only showing top 3 rows | 3.7 |
| Đoạn mã 5.16 | Lưu và nạp lại PipelineModel. | ĐẠT |  | 8.8 |
| Đoạn mã 5.17 | Khung winsorize cho cột thu nhập. | ĐẠT |  | 0.6 |
| Đoạn mã 5.18 | Khung pipeline tiền xử lý cho bài toán churn. | ĐẠT |  | 6.6 |
| Đoạn mã 5.19 | Đoạn mã chuẩn hóa có một lỗi phương pháp nghiêm trọng. | BỎ QUA | ví dụ về LỖI phương pháp (fit scaler trên toàn bộ dữ liệu) – không nên chạy theo | 0.0 |
| Đoạn mã 6.1 | Khởi tạo phiên làm việc và chia dữ liệu huấn luyện/kiểm tra. | ĐẠT | So ban ghi kiem tra : 3783 | 15.5 |
| Đoạn mã 6.2 | Huấn luyện hồi quy logistic dự đoán khách hàng rời bỏ. | ĐẠT | only showing top 5 rows | 17.4 |
| Đoạn mã 6.3 | Huấn luyện cây quyết định và in cấu trúc luật. | ĐẠT | only showing top 5 rows | 10.3 |
| Đoạn mã 6.4 | Huấn luyện rừng ngẫu nhiên và xem độ quan trọng đặc trưng. | ĐẠT | so_lan_goi_ho_tro -> 0.5911 | 37.8 |
| Đoạn mã 6.5 | Hồi quy tuyến tính dự đoán giá nhà và đánh giá bằng RegressionEvaluator. | ĐẠT | R2  : 0.9231019094492374 | 3.7 |
| Đoạn mã 6.6 | Hồi quy GBT dự đoán giá nhà và so sánh với hồi quy tuyến tính. | ĐẠT | (5,[0,1,2,3,4],[0.5332657960731245,0.059651807067040416,0.05914855804385247,0.21 | 84.2 |
| Đoạn mã 6.7 | Đánh giá và so sánh các mô hình phân loại churn. | ĐẠT | +-----+----------+-----+ | 12.0 |
| Đoạn mã 6.8 | Quy trình tinh chỉnh hoàn chỉnh với Pipeline, ParamGridBuilder và CrossValidator. | ĐẠT | AUC tren tap kiem tra: 0.7562453415687966 | 1139.1 |
| Đoạn mã 6.9 | Quy trình hoàn chỉnh dự đoán khách hàng rời bỏ: từ dữ liệu thô tới mô hình lưu trữ và dự đoán theo lô. | ĐẠT | Do quan trong dac trung: (13,[0,1,2,3,4,5,6,7,9,10,11],[0.08522294759624616,0.19 | 220.5 |
| Đoạn mã 7.1 | Khảo sát WSSSE và hệ số silhouette theo số cụm K. | ĐẠT | k = 10 / WSSSE = 12208.0 / silhouette = 0.396 | 102.4 |
| Đoạn mã 7.2 | Quy trình phân cụm khách hàng hoàn chỉnh với Pipeline. | ĐẠT | +----------+-----+ | 8.4 |
| Đoạn mã 7.3 | Khai phá tập mục phổ biến và luật kết hợp bằng FPGrowth. | ĐẠT | +-----+----------------------+----------+ | 7.0 |
| Đoạn mã 7.4 | Huấn luyện ALS trên MovieLens và sinh gợi ý. | ĐẠT | only showing top 5 rows | 35.3 |
| Đoạn mã 7.5 | Khung tính bảng RFM và vòng lặp chọn K. | ĐẠT | 8 815.2397507757365 0.47310583500141346 | 65.0 |
| Đoạn mã 7.6 | Khung lời giải bài tập ALS. | ĐẠT | +------+------------------------------------+ | 11.1 |
| Đoạn mã 8.1 | Suy luận phân tán mô hình Keras trên Spark bằng mapInPandas. | BỎ QUA | cần TensorFlow + mô hình đã huấn luyện (GPU) | 0.0 |
| Đoạn mã 8.2 | Khung huấn luyện phân tán PyTorch với TorchDistributor (Spark 3.4 trở lên). | BỎ QUA | cần cụm GPU và hàm build_model, make_dataloader của người học | 0.0 |
| Đoạn mã 8.3 | Khung huấn luyện Keras phân tán với Horovod. | BỎ QUA | cần Horovod + GPU | 0.0 |
| Đoạn mã 8.4 | Theo dõi thí nghiệm và đăng ký mô hình Keras với MLflow. | BỎ QUA | cần TensorFlow + MLflow server | 0.0 |
| Đoạn mã 8.5 | Suy luận phân tán bằng mapInPandas. | BỎ QUA | cần TensorFlow + mô hình đã huấn luyện | 0.0 |
