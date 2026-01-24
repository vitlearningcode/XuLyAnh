import cv2 as cv
import numpy as np

img = cv.imread('fish.jpg')
rows, cols = img.shape[:2]

# Tạo 2 ma trận map_x và map_y chứa tọa độ mới cho từng pixel
map_x = np.zeros((rows, cols), np.float32)
map_y = np.zeros((rows, cols), np.float32)

# Tạo quy luật biến đổi (ví dụ: lượn sóng theo trục x)
for i in range(rows):
    for j in range(cols):
        # map_x[i, j] = j  # Giữ nguyên hoành độ (nếu muốn)
        # Tạo hiệu ứng sóng: pixel tại (i,j) sẽ lấy màu từ vị trí bị lệch đi một chút
        map_x[i, j] = j + 10 * np.sin(i / 10.0) 
        map_y[i, j] = i

# Áp dụng remap
dst = cv.remap(img, map_x, map_y, cv.INTER_LINEAR)

cv.imshow('window', dst)
cv.waitKey(0)
cv.destroyAllWindows()