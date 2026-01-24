import cv2 as cv
import numpy as np

img = cv.imread('fish.jpg') # Đảm bảo bạn có file ảnh 'fish.jpg' hoặc thay bằng ảnh khác
h, w = img.shape[:2]

# Dịch chuyển ảnh: x = 100 pixel, y = 50 pixel
x, y = 100, 50
# Tạo ma trận dịch chuyển [[1, 0, x], [0, 1, y]]
M = np.float32([[1, 0, x], [0, 1, y]])

# Áp dụng biến đổi
shifted = cv.warpAffine(img, M, (w, h))

cv.imshow('window', shifted)
cv.waitKey(0)
cv.destroyAllWindows()