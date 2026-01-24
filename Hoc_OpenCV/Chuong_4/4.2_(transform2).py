import cv2 as cv

def trackbar(angle):
    # Tạo ma trận xoay: (tâm xoay, góc xoay, tỉ lệ)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(img, M, (w, h))
    cv.imshow('window', rotated)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]
center = (w // 2, h // 2) # Tâm xoay là giữa ảnh

cv.imshow('window', img)
# Tạo trackbar để chỉnh góc xoay từ 0 đến 180 độ
cv.createTrackbar('angle', 'window', 0, 180, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()