# Add a trackbar
import cv2 as cv
import numpy as np

img = np.fromfunction(lambda i, j: j, (50, 256), dtype='uint8')

modes = (cv.THRESH_BINARY,
    cv.THRESH_BINARY_INV,
    cv.THRESH_TRUNC,
    cv.THRESH_TOZERO,
    cv.THRESH_TOZERO_INV)

def trackbar(x):
    """Trackbar callback function."""
    text = f'threshold={x}'
    #cv.displayOverlay('window', text, 1000)
   # cv.setWindowTitle('window', f'Thresholding Demo - threshold={x}')
    cv.setWindowTitle('window', text) #thay bằng lệnh này chạy vì cái displayOverlay kia khi cài bằng pip đang bị lỗi!
    ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
    ret, img3 = cv.threshold(img, x, 255, cv.THRESH_TRUNC)
    ret, img4 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
    ret, img5 = cv.threshold(img, x, 255, cv.THRESH_TOZERO_INV)
    cv.imshow('window', np.vstack([img, img1, img2, img3, img4, img5]))

cv.imshow('window', img)
trackbar(100)
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()

# import cv2 as cv

# img = cv.imread('lego.png', 0) # Đọc ảnh xám
# if img is not None:
#     # Các ví dụ trong file PDF:
#     _, t1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#     _, t2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
#     _, t3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
    
#     cv.imshow('Binary', t1)
#     cv.imshow('Binary Inv', t2)
#     cv.imshow('Trunc', t3)
#     cv.waitKey(0)