import cv2 as cv
import numpy as np

RED = (0, 0, 255)
p0, p1 = (0, 0), (0, 0)

def mouse(event, x, y, flags, param):
    global p0, p1
    if event == cv.EVENT_LBUTTONDOWN:
        p0 = (x, y)
        p1 = (x, y)
    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        p1 = (x, y)
    
    img[:] = 0
    cv.line(img, p0, p1, RED, 10)
    cv.imshow('window', img)

img = np.zeros((100, 500, 3), np.uint8)
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()