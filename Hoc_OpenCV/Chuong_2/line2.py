import cv2 as cv
import numpy as np

RED = (0, 0, 255)
p0, p1 = (100, 30), (400, 90)

def trackbar(x):
    x = max(1, x) # Độ dày tối thiểu là 1
    img[:] = 0    # Xóa ảnh (về màu đen)
    cv.line(img, p0, p1, RED, x)
    cv.imshow('window', img)

img = np.zeros((100, 500, 3), np.uint8)
cv.line(img, p0, p1, RED, 2)
cv.imshow('window', img)

cv.createTrackbar('thickness', 'window', 2, 20, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()