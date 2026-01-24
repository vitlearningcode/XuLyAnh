import cv2 as cv
import numpy as np

img = cv.imread('lego.png')
# Tách thành 3 kênh
b, g, r = cv.split(img)

# Hiển thị 3 kênh (chúng sẽ hiển thị dưới dạng ảnh xám)
img2 = np.hstack([b, g, r])
cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()