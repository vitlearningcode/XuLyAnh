import cv2 as cv
import numpy as np

# Đọc ảnh (bạn cần có file 'legos.jpg' hoặc thay bằng ảnh khác)
img = cv.imread('legos.jpg')
# Chuyển sang không gian màu HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

def trackbar(x):
    # Định nghĩa ngưỡng dưới và trên cho màu cần lọc
    lower = np.array([x, 30, 30])
    upper = np.array([x + 5, 250, 250])
    
    # Tạo mặt nạ (mask) cho các pixel nằm trong ngưỡng
    mask = cv.inRange(hsv, lower, upper)
    
    # Áp dụng mặt nạ lên ảnh gốc
    img2 = cv.bitwise_and(img, img, mask=mask)
    
    # Hiển thị ảnh gốc và ảnh đã lọc chồng lên nhau (hoặc cạnh nhau)
    cv.imshow('window', np.vstack([img, img2]))

cv.imshow('window', img)
# Hue trong OpenCV có giá trị từ 0 đến 179
cv.createTrackbar('hue', 'window', 0, 179, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()