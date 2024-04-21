import cv2

# Khởi tạo face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Khởi tạo webcam hoặc đọc video từ file
cap = cv2.VideoCapture(0)  # Sử dụng webcam

face_count = 0  # Đếm số lượng khuôn mặt đã lưu
faces_saved = []  # Danh sách lưu các khuôn mặt đã nhận diện
is_detect=None
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('images/student_capture.avi', cv2.VideoWriter_fourcc(*'DIVX'),25, (width, height))


while True:
    ret, frame = cap.read()  # Đọc một frame từ video

    # Chuyển đổi frame sang ảnh grayscale để nhận diện khuôn mặt
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Nhận diện khuôn mặt
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    face_detected = len(faces) > 0

    for (x, y, w, h) in faces:
        # Vẽ hình chữ nhật xung quanh khuôn mặt
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_img = frame
        # writer = cv2.VideoWriter(f'images/student_capture{face_count}.mp4', cv2.VideoWriter_fourcc(*'DIVX'),25, (w, h))
        if face_detected:
            writer.write(face_img)
        else:
            writer.release()


        # cv2.imwrite(f'face_{face_count}.jpg', face_img)
        # face_count += 1




    # Hiển thị frame
    cv2.imshow('Face Detection', frame)

    # Thoát khỏi vòng lặp nếu nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng video capture và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
