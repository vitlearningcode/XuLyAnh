import cv2 as cv
import numpy as np

# Ảnh màu đen
img = np.zeros((100, 500, 3), np.uint8)
cv.imshow('RGB', img)

# Ảnh xám đen
gray_img = np.zeros((100, 500), np.uint8)
cv.imshow('Gray', gray_img)

cv.waitKey(0)
cv.destroyAllWindows()