import cv2 as cv
import numpy as np

RED = (0, 0, 255)
# Điểm khởi đầu và kết thúc mặc định
p0, p1 = (100, 30), (400, 90)

def mouse(event, x, y, flags, param):
    global p0, p1
    if event == cv.EVENT_LBUTTONDOWN:
        p0 = (x, y)
        p1 = (x, y)
    elif event == cv.EVENT_MOUSEMOVE and flags == 1: # Kéo chuột
        p1 = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        p1 = (x, y)
    
    # Tính toán góc và độ dài dựa trên 2 điểm p0, p1
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    angle = np.degrees(np.arctan2(dy, dx))
    length = np.sqrt(dx**2 + dy**2) / 50 # Tỉ lệ
    
    cv.displayOverlay('window', f'angle={angle:.1f}, len={length:.1f}')
    
    # Tạo ma trận biến đổi và áp dụng
    M = cv.getRotationMatrix2D(p0, angle, length)
    img2 = cv.warpAffine(img, M, (w, h))
    
    # Vẽ đường thẳng minh họa
    cv.line(img2, p0, p1, RED, 2)
    cv.imshow('window', img2)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()