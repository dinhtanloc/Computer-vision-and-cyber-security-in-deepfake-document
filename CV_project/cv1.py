import numpy as np
import cv2

# Khởi tạo camera
cap = cv2.VideoCapture(0)  # 0 là ID của camera mặc định

# Đọc frame đầu tiên
ret, frame1 = cap.read()
prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    # Đọc frame tiếp theo
    ret, frame2 = cap.read()
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Tính toán optical flow sử dụng thuật toán Farnebäck
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Hiển thị vector chuyển động trên hình ảnh
    h, w = gray.shape[:2]
    y, x = np.mgrid[0:h:10, 0:w:10].reshape(2, -1).astype(int)
    fx, fy = flow[y, x].T

    # Vẽ các vector chuyển động lên hình ảnh
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.polylines(vis, lines, 0, (0, 255, 0))

    # Hiển thị hình ảnh với các vector chuyển động
    cv2.imshow('Optical Flow', vis)

    # Cập nhật frame trước để sử dụng trong lần lặp tiếp theo
    prev_gray = gray

    # Điều kiện dừng: nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng tất cả cửa sổ
cap.release()
cv2.destroyAllWindows()