import cv2 as cv
import numpy as np

RED = (0, 0, 255)
BLUE = (255, 0, 0)
p0, p1 = (0, 0), (0, 0)

def mouse(event, x, y, flags, param):
    global p0, p1, img
    
    if event == cv.EVENT_LBUTTONDOWN:
        p0 = (x, y)
        p1 = (x, y)
    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = (x, y)
        img[:] = img0[:] # Khôi phục ảnh cũ
        cv.line(img, p0, p1, BLUE, 2) # Vẽ nét tạm màu xanh
    elif event == cv.EVENT_LBUTTONUP:
        p1 = (x, y)
        img[:] = img0[:]
        cv.line(img, p0, p1, RED, 4) # Vẽ nét thật màu đỏ
        img0[:] = img[:] # Lưu lại vào img0

    cv.imshow('window', img)

img0 = np.zeros((100, 500, 3), np.uint8)
img = img0.copy()
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()