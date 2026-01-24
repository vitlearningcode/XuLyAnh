import cv2 as cv
import numpy as np

d = 15
# Tạo ảnh nền đen kích thước 100x100
rect = np.zeros((100, 100), np.uint8)
# Vẽ hình chữ nhật trắng
cv.rectangle(rect, (d, d), (100-d, 100-d), 255, -1)

# Tạo ảnh khác với hình tròn trắng
circle = np.zeros((100, 100), np.uint8)
cv.circle(circle, (50, 50), 40, 255, -1)

# Thực hiện các phép toán bit
bit_and = cv.bitwise_and(rect, circle) # Giao
bit_or = cv.bitwise_or(rect, circle)   # Hợp
bit_xor = cv.bitwise_xor(rect, circle) # Loại trừ

# Hiển thị tất cả kết quả
img = np.hstack([rect, circle, bit_and, bit_or, bit_xor])
cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()