import cv2 as cv
import numpy as np

def trackbar(x):
    # Cập nhật kênh Value (kênh thứ 2 trong HSV)
    img[:, :, 2] = x
    # Chuyển đổi từ HSV sang BGR để hiển thị
    rgb = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    cv.imshow('window', rgb)

# HSV Hue channel chỉ đi từ 0-179 trong OpenCV
img = np.zeros((180, 256, 3), dtype=np.uint8)

# Tạo gradient cho Hue và Saturation
for i in range(180):
    img[i, :, 0] = i # Hue
for i in range(256):
    img[:, i, 1] = i # Saturation

cv.imshow('window', img)
cv.createTrackbar('value', 'window', 0, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()