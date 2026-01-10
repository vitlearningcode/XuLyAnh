import cv2 as cv
import numpy as np

GREEN = (0, 255, 0)
p0 = (100, 30)

def mouse(event, x, y, flags, param):
    if flags == 1: # Đang giữ chuột trái
        p1 = (x, y)
        img[:] = 0
        cv.line(img, p0, p1, GREEN, 10)
        cv.imshow('window', img)

img = np.zeros((100, 500, 3), np.uint8)
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()