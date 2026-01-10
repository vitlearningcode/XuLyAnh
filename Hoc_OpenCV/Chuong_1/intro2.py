import cv2 as cv

cap = cv.VideoCapture(0) # 0 là webcam mặc định

while True:
    # Đọc từng khung hình
    ret, frame = cap.read()
    if not ret: break

    # Chuyển sang ảnh xám
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Hiển thị
    cv.imshow('frame', gray) # Lưu ý: biến frame ở đây hiển thị ảnh gốc, nếu muốn xám thì thay bằng gray

    # Nhấn 'q' để thoát
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()