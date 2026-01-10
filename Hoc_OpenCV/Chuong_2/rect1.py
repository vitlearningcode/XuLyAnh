import cv2 as cv
import numpy as np

# Định nghĩa màu
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
p0, p1 = (0,0), (0,0)

def draw(x=None):
    pass # Hàm giả chỉ để trackbar gọi

def mouse(event, x, y, flags, param):
    global p0, p1, img
    
    # Lấy giá trị từ trackbar
    d = cv.getTrackbarPos('thickness', 'window')
    if d == 0: d = -1 # Nếu 0 thì vẽ đặc (-1)
    
    i = cv.getTrackbarPos('color', 'window')
    color = colors[i]

    if event == cv.EVENT_LBUTTONDOWN:
        p0 = (x, y)
        p1 = (x, y)
    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = (x, y)
        img[:] = img0[:]
        cv.rectangle(img, p0, p1, color, d)
    elif event == cv.EVENT_LBUTTONUP:
        p1 = (x, y)
        img[:] = img0[:]
        cv.rectangle(img, p0, p1, color, d)
        img0[:] = img[:]
        
    cv.imshow('window', img)

img0 = np.zeros((200, 500, 3), np.uint8)
img = img0.copy()
cv.imshow('window', img)

cv.createTrackbar('color', 'window', 0, 6, draw)
cv.createTrackbar('thickness', 'window', 0, 10, draw)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()