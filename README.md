BẢN MÔ TẢ ĐỒ ÁN MÔN HỌC
===================

> *Đề tài: Phân loại văn bản Tiếng Việt*

# Danh sách thành viên

- Đinh Thế Anh

- Hoàng Văn Khoa

- Trương Bảo Thắng

- Ngô Văn Thủy

# Mô tả bài toán thực tế

## Mục đích

Mục đích của đề tài là xây dựng được một công cụ để phân loại các văn bản Tiếng
Việt theo nội dung.

## Yêu cầu

Xây dựng được một công cụ (có giao diện dòng lệnh hoặc đồ họa) có khả năng phân
loại các văn bản Tiếng Việt vào các nhóm.

## Kịch bản

Hoạt động của chương trình gồm hai quá trình: quá trình học và quá trình kiểm
chứng.
- Quá trình học: Dùng tập học để huấn luyện hệ thống. Đầu ra của quá trình học
là một dạng biểu diễn của hàm mục tiêu.
- Quá trình kiểm chứng: Sử dụng hàm mục tiêu đối với tập kiểm chứng thu được
kết quả phân loại. So sánh kết quả phân loại này với kết quả có sẵn trên tập
kiểm chứng để đánh giá hiệu quả của hệ thống.

# Sơ lược về giải pháp

Giải pháp là sử dụng phương pháp học có giám sát Naïve Bayes.
Công cụ này được lập trình bằng ngôn ngữ Python và ngôn ngữ C/C++. Nhóm sẽ sử
dụng thư viện Đông Du viết bằng C/C++ để tách từ.
Công cụ sử dụng các thư viện sau:
- Các thư viện của Python, thông tin tại https://pypi.python.org/pypi
- Thư viện xử lí ngôn ngữ Tiếng Việt Đông Du: http://viet.jnlp.org/dongdu. Tuy
nhiên, bọn em sử dụng một bản đã được sửa đổi của thư viện này để có thể
gọi thư viện từ Python.
- Một số kết quả trong đồ án của môn Học máy (có sự tham gia của thành viên
trong nhóm là Hoàng Văn Khoa).


## Thông tin đầu vào/đầu ra

- Đầu vào của quá trình học là một tập học. Đầu ra của quá trình này là một
dạng của hàm mục tiêu.

- Đầu vào của quá trình kiểm chứng là một tập dữ liệu kiểm chứng và hàm mục
tiêu. Đầu ra là kết quả phân loại của hệ thống và đánh giá hiệu quả của hệ
thống.
