import cv2 as cv
import numpy as np

# Mảng lưu 4 điểm chọn
pts = []

def mouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)
        pts.append([x, y])
        cv.imshow('image', img)
        
        # Khi đủ 4 điểm thì thực hiện biến đổi
        if len(pts) == 4:
            pts1 = np.float32(pts)
            # Giả sử muốn output ra ảnh kích thước 400x300
            pts2 = np.float32([[0, 0], [400, 0], [0, 300], [400, 300]])
            
            M = cv.getPerspectiveTransform(pts1, pts2)
            dst = cv.warpPerspective(clone, M, (400, 300))
            cv.imshow('output', dst)

img = cv.imread('sudoku.jpg') # Thay bằng ảnh tài liệu/giấy bất kỳ
clone = img.copy() # Giữ bản gốc để warp
cv.imshow('image', img)
cv.setMouseCallback('image', mouse)

cv.waitKey(0)
cv.destroyAllWindows()