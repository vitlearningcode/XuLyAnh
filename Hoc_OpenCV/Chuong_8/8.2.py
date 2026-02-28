import cv2 as cv
import numpy as np
import time

path=cv.data.haarcascades + "haarcascade_frontalface_default.xml"
face_detector=cv.CascadeClassifier(path)
# CẢI TIẾN: Kiểm tra xem bộ phân loại có được tải thành công không
if face_detector.empty():
    print("Lỗi: Không thể tải file cascade của bộ nhận diện khuôn mặt.")
    exit()

# CẢI TIẾN: Biến hàm `detect` thành một hàm độc lập, dễ tái sử dụng.
# Nó nhận một khung hình (frame) làm đầu vào và trả về các hình chữ nhật đã phát hiện.
def detect_faces(img):
    rects=face_detector.detectMultiScale(img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags=cv.CASCADE_SCALE_IMAGE)
    return rects
        
cap=cv.VideoCapture(0)
# CẢI TIẾN: Kiểm tra xem camera có mở được không
if not cap.isOpened():
    print("Lỗi: Không thể mở camera.")
    exit()

M=np.float32([[0.5,0,0],[0,0.5,0]])
size=(640,360)

t0=time.time()
while True:
    # Đọc từng khung hình
    ret,frame=cap.read()
    # LỖI CHÍNH: Thiếu kiểm tra `ret`. Nếu không đọc được frame, chương trình sẽ sập.
    # SỬA LỖI: Thêm đoạn kiểm tra này để thoát một cách an toàn.
    if not ret:
        print("Không thể nhận khung hình (kết thúc stream?). Đang thoát...")
        break

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray_s=cv.warpAffine(gray,M,size)
    
    # Vẽ các hình chữ nhật lên khung hình đã thu nhỏ
    face_rects = detect_faces(gray_s)
    for rect in face_rects:
        cv.rectangle(gray_s,rect,255,2)

    cv.imshow('window',gray_s)
    t = time.time()
    # CẢI TIẾN: Hiển thị FPS (khung hình/giây) là một chỉ số trực quan hơn
    fps = 1 / (t - t0)
    cv.setWindowTitle('window', f'FPS: {fps:.2f}')
    t0 = t
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()