# binary thresholding
import cv2 as cv
import numpy as np

def trackbar(x):
    ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
    cv.imshow('window', np.hstack([img, img1, img2]))
    text = f'threshold={x}, mode=BINARY | BINARY_INV'
    cv.setWindowTitle('window', text)

# đọc ảnh
img = cv.imread('eye.jpg', cv.IMREAD_GRAYSCALE)

# kiểm tra ảnh
if img is None:
    print("Không đọc được ảnh!")
    exit()

# tạo cửa sổ
cv.namedWindow('window', cv.WINDOW_NORMAL) #nếu hình quá bự thì dùng cái này kéo khung ra


# gọi lần đầu
trackbar(100)

# tạo trackbar
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()
