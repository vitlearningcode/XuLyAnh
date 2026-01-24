import cv2 as cv
import numpy as np

img = cv.imread('sudoku.jpg') # Bạn có thể dùng ảnh tờ giấy, bảng, hoặc 'sudoku.jpg'
rows, cols = img.shape[:2]

# Chọn 4 điểm trên ảnh gốc (dữ liệu này bạn cần lấy tọa độ thực tế từ ảnh của mình)
# Ví dụ: góc trên-trái, trên-phải, dưới-trái, dưới-phải của vùng cần cắt
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

# Chọn 4 điểm đích tương ứng (muốn biến nó thành hình vuông 300x300)
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Tạo ma trận biến đổi phối cảnh (3x3)
M = cv.getPerspectiveTransform(pts1, pts2)

# Áp dụng biến đổi
dst = cv.warpPerspective(img, M, (300, 300))

# Vẽ các điểm đã chọn lên ảnh gốc để dễ nhìn
for p in pts1:
    cv.circle(img, (int(p[0]), int(p[1])), 5, (0, 0, 255), -1)

cv.imshow('Original', img)
cv.imshow('Perspective', dst)
cv.waitKey(0)
cv.destroyAllWindows()