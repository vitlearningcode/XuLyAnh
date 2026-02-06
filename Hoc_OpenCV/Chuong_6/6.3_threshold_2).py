# threshold to zero
import cv2 as cv
import numpy as np

def trackbar(x):
    _, img1 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
    _, img2 = cv.threshold(img, x, 255, cv.THRESH_TOZERO_INV)

    show = np.hstack([img, img1, img2])
    show = cv.resize(show, None, fx=0.4, fy=0.4)

    cv.imshow('window', show)
    text =  f'threshold={x}, mode=TOZERO | TOZERO_INV'
    cv.setWindowTitle(
        'window',
       text
    )

# đọc ảnh grayscale
img = cv.imread('eye.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Không đọc được ảnh")
    exit()

# tạo cửa sổ
cv.namedWindow('window', cv.WINDOW_NORMAL)

# gọi lần đầu
trackbar(100)

# tạo trackbar
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()
