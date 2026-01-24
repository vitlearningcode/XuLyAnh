import cv2 as cv
import numpy as np

img = cv.imread('fish.jpg')
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

# Tạo mặt nạ đen cùng kích thước với ảnh (chỉ lấy 2 chiều đầu tiên h, w)
mask = np.zeros(img.shape[:2], dtype='uint8')
# Vẽ hình tròn trắng lên mặt nạ (khu vực muốn giữ lại)
cv.circle(mask, (60, 50), 50, 255, -1)

# Áp dụng mặt nạ lên ảnh gốc bằng phép AND
masked = cv.bitwise_and(img, img, mask=mask)

img2 = np.hstack([img, masked])
cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()