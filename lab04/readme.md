# 1. CÔNG NGHỆ SỬ DỤNG
- Ngôn ngữ lập trình: Python
- Thư viện tính toán số: numpy
- Thư viện đồ họa và trực quan hóa: matplotlib.pyplot (để tạo biểu đồ và hình ảnh minh họa quá trình tiến hóa) và sử dụng mpl_toolkits.mplot3d cho các biểu đồ 3D khi cần.
- Thư viện cơ bản: random

# 2. GIẢI THÍCH CÁCH HOẠT ĐỘNG
- Trong LAB này, triển khai Giải thuật Di truyền (GA) để giải quyết các bài toán tối ưu hóa hàm số, minh họa cách GA mô phỏng quá trình tiến hóa tự nhiên để tìm kiếm giải pháp tối ưu. Cơ chế hoạt động chung của GA trong các ví dụ bao gồm các bước lặp đi lặp lại:
+ Khởi tạo quần thể: Thuật toán bắt đầu bằng việc tạo ra một tập hợp các cá thể (solutions) ngẫu nhiên. Mỗi cá thể đại diện cho một giải pháp tiềm năng cho bài toán. Ví dụ, trong bài toán tối ưu hóa hàm f(x), một cá thể là một giá trị x; với hàm g(x,y), một cá thể là một cặp (x,y); và với mã hóa nhị phân, một cá thể là một chuỗi bit.
+ Đánh giá độ thích nghi (Fitness Evaluation): Mỗi cá thể trong quần thể được gán một "điểm fitness" bằng cách tính giá trị của hàm mục tiêu mà chúng ta muốn tối ưu.
+ Chọn lọc (Selection): Các cá thể có điểm fitness cao hơn (tức là giải pháp tốt hơn) sẽ có cơ hội cao hơn để được chọn làm "cha mẹ" cho thế hệ tiếp theo. Điều này mô phỏng nguyên lý chọn lọc tự nhiên "kẻ mạnh sinh tồn".
+ Lai ghép (Crossover): Hai cá thể cha mẹ được chọn sẽ kết hợp "gen" của chúng để tạo ra (các) cá thể con mới, mang đặc điểm từ cả hai.
+ Đột biến (Mutation): Sau khi lai ghép, các cá thể con có thể trải qua đột biến, tức là một sự thay đổi ngẫu nhiên nhỏ trong gen của chúng.
+ Tạo thế hệ mới: Các cá thể con mới được tạo ra thông qua lai ghép và đột biến sẽ thay thế quần thể hiện tại để tạo thành thế hệ tiếp theo.
+ Lặp lại: Quá trình từ bước 2 đến 6 được lặp đi lặp lại qua một số lượng thế hệ nhất định. Với mỗi thế hệ, quần thể sẽ dần "tiến hóa", và các giải pháp tốt nhất sẽ dần hội tụ về vùng tối ưu của hàm mục tiêu.
- Trực quan hóa: Xuyên suốt LAB, matplotlib được sử dụng để vẽ biểu đồ sự thay đổi của giá trị fitness tốt nhất qua các thế hệ. Biểu đồ này giúp chúng ta dễ dàng quan sát quá trình hội tụ của thuật toán và đánh giá hiệu quả của các tham số đã chọn.

# 3. KẾT QUẢ
Mỗi ví dụ và bài tập trong LAB này đều in ra kết quả của cá thể tốt nhất và giá trị fitness tương ứng sau mỗi thế hệ, cũng như kết quả cuối cùng. Đồng thời, biểu đồ sẽ được tạo để trực quan hóa sự thay đổi của giá trị fitness tốt nhất qua các thế hệ. Điều này cho phép quan sát rõ ràng quá trình hội tụ của thuật toán di truyền về giải pháp tối ưu. Kết quả cho thấy GA có khả năng tìm ra các giá trị gần với nghiệm chính xác (hoặc nghiệm chính xác nếu hàm đơn giản và đủ thế hệ) sau một số lượng thế hệ nhất định.
