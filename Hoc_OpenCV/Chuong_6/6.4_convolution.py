# convolution (mean filter)
import cv2 as cv
import numpy as np

def trackbar(x):
    d = 2 * x + 1              # đảm bảo kernel lẻ: 1,3,5,7...
    kernel = np.ones((d, d), np.float32) / (d * d)

    img1 = cv.filter2D(img, -1, kernel)

    show = np.hstack([img, img1])
    show = cv.resize(show, None, fx=0.4, fy=0.4)

    cv.imshow('window', show)
    cv.setWindowTitle('window', f'kernel = {d} x {d}')

# đọc ảnh grayscale
img = cv.imread('eye.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Không đọc được ảnh")
    exit()

# tạo window
cv.namedWindow('window', cv.WINDOW_NORMAL)

# gọi lần đầu
trackbar(2)

# trackbar điều chỉnh kernel size
cv.createTrackbar('kernel', 'window', 2, 7, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()
