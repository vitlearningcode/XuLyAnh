import cv2 as cv
import numpy as np

img = cv.imread('lego.png')
# Tạo mảng số 0 (màu đen) có kích thước bằng 1 kênh của ảnh
z = np.zeros(img.shape[:2], 'uint8')
b, g, r = cv.split(img)

# Gộp lại nhưng thay các kênh khác bằng màu đen
blue = cv.merge([b, z, z])
green = cv.merge([z, g, z])
red = cv.merge([z, z, r])

img2 = np.hstack([blue, green, red])
cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()