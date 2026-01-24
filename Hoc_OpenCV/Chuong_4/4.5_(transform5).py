import cv2 as cv
import numpy as np

img = cv.imread('fish.jpg')
# Thay đổi kích thước ảnh cho dễ nhìn
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

# Tạo một ma trận có cùng kích thước với ảnh, mỗi pixel có giá trị 40
M = np.ones(img.shape, dtype='uint8') * 40

# Cộng thêm 40 vào mỗi pixel (làm sáng)
brighter = cv.add(img, M)
# Trừ đi 40 ở mỗi pixel (làm tối)
darker = cv.subtract(img, M)

# Ghép các ảnh lại theo chiều ngang để hiển thị
img2 = np.hstack([img, brighter, darker])

cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()