import cv2 as cv
import numpy as np

def trackbar(x):
    # Cập nhật kênh màu Đỏ (kênh thứ 2 trong BGR) với giá trị từ trackbar
    img[:, :, 2] = x
    cv.imshow('window', img)

# Khởi tạo ảnh đen
img = np.zeros((256, 256, 3), dtype=np.uint8)

# Tạo gradient cho kênh Blue (0) và Green (1)
for i in range(256):
    img[i, :, 0] = i  # Kênh Blue thay đổi theo dòng
    img[:, i, 1] = i  # Kênh Green thay đổi theo cột

cv.imshow('window', img)
# Tạo trackbar để điều chỉnh màu đỏ từ 0 đến 255
cv.createTrackbar('red', 'window', 0, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()