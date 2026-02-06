# morphological transformation : erode
import cv2 as cv
import numpy as np

def trackbar(x):
    n = 2 * x + 1                      # kernel size lẻ
    kernel = np.ones((n, n), np.uint8)

    img1 = cv.erode(img, kernel, iterations=1)

    show = np.hstack([img, img1])
    show = cv.resize(show, None, fx=0.5, fy=0.5)

    cv.imshow('window', show)
    cv.setWindowTitle('window', f'Erode | kernel = {n} x {n}')

# đọc ảnh grayscale
img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Không đọc được ảnh")
    exit()

# tạo window
cv.namedWindow('window', cv.WINDOW_NORMAL)

# gọi lần đầu
trackbar(2)

# trackbar điều chỉnh kernel
cv.createTrackbar('kernel', 'window', 2, 5, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()
