# image gradient - Canny kết hợp làm mịn, gradient và ngưỡng kép nên ít nhiễu và biên mảnh hơn.
import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Không đọc được ảnh")
    exit()

edges = cv.Canny(img, 100, 200)

show = np.hstack([img, edges])
show = cv.resize(show, None, fx=0.5, fy=0.5)

cv.imshow('window', show)
cv.setWindowTitle('window', 'Original | Canny (100, 200)')

cv.waitKey(0)
cv.destroyAllWindows()
