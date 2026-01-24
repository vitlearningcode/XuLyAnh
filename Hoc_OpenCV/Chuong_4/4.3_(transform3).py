import cv2 as cv

def trackbar(scale):
    # Chia cho 10 để có giá trị thập phân (ví dụ 10 -> 1.0)
    s = scale / 10.0
    # Góc xoay là 0, chỉ thay đổi tỉ lệ (s)
    M = cv.getRotationMatrix2D(center, 0, s)
    rotated = cv.warpAffine(img, M, (w, h))
    cv.imshow('window', rotated)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]
center = (w // 2, h // 2)

cv.imshow('window', img)
# Trackbar chạy từ 10 (tỉ lệ 1.0) đến 30 (tỉ lệ 3.0)
cv.createTrackbar('scale', 'window', 10, 30, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()