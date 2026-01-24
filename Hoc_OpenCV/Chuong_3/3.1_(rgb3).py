import cv2 as cv
import numpy as np

# Tạo các mảng 2 chiều cho từng kênh màu
z = np.zeros((256, 256), dtype=np.uint8)
# Tạo gradient theo chiều dọc và ngang (dựa trên OCR và logic thông thường)
h = np.fromfunction(lambda i, j: i, (256, 256), dtype=np.uint8)
v = np.fromfunction(lambda i, j: j, (256, 256), dtype=np.uint8)

# Gộp các kênh lại thành ảnh BGR
img = cv.merge([z, h, v])

cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()