# 1. Công nghệ sử dụng:
- Bài toán 4-Queens và 8-Queens trong bài thực hành sử dụng:
  + Ngôn ngữ lập trình python.
  + Sử dụng các thư viện: numpy, random
  + Sử  dụng kỹ thuật Backtracking (quay lui).

# 2. Giải thích cách hoạt động:
- Chương trình tìm cách đặt N quân hậu lên bàn cờ NxN sao cho không quân hậu nào tấn công quân hậu khác. Tức là không có 2 quân hậu nào nằm trên cùng hàng, cùng cột hoặc cùng đường chéo.
- Cách hoạt động theo từng bước:
  + Hàm solve(num_queens): Gọi hàm search() để bắt đầu tìm lời giải từ trạng thái rỗng (state = []).
  + Hàm search(state, solutions, num_queens):
      Nếu trạng thái hiện tại là hợp lệ (đã đặt đủ N quân hậu), thì thêm lời giải vào danh sách solutions.
      Nếu chưa đủ, tìm tất cả vị trí cột có thể đặt quân hậu tại hàng hiện tại bằng get_candidates(...).
  + Hàm get_candidates(state, num_queens): Trả về danh sách các cột mà quân hậu có thể được đặt mà không bị tấn công bởi các quân hậu đã được đặt trước đó. Loại bỏ các cột trùng, các đường chéo chính và phụ.
  + Backtracking (quay lui):
      Mỗi khi đặt một quân hậu, chương trình gọi lại chính nó để đặt quân hậu tiếp theo.
      Nếu đi vào ngõ cụt (không có vị trí nào phù hợp), nó sẽ quay lui (bỏ quân hậu vừa đặt) và thử hướng đi khác.
  + In kết quả:
      Bài 4-Queens: In toàn bộ lời giải và tọa độ các quân hậu.
      Bài 8-Queens: In tổng số lời giải và chọn ngẫu nhiên 2 lời giải để minh họa.
    
