import cv2 as cv
import numpy as np

pts = []
img = np.zeros((400, 600, 3), np.uint8)

def draw(x=None):
    img[:] = 0 # Xóa màn hình
    if len(pts) > 0:
        cv.polylines(img, np.array([pts]), True, (0, 255, 0), 2)
    cv.imshow('window', img)

def mouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        pts.append((x, y))
        draw()

cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()