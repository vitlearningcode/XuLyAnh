# image gradient - Laplacian
import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Không đọc được ảnh")
    exit()

# Laplacian (dùng depth signed)
lap = cv.Laplacian(img, cv.CV_64F)

# chuyển về uint8 để hiển thị
lap = np.uint8(np.absolute(lap))

show = np.hstack([img, lap])
show = cv.resize(show, None, fx=0.5, fy=0.5)

cv.imshow('window', show)
cv.setWindowTitle('window', 'Original | Laplacian')

cv.waitKey(0)
cv.destroyAllWindows()
