import cv2 as cv
import numpy as np

RED = (0, 0, 255)
pts = np.array([(50, 50), (300, 190), (400, 10)], np.int32)
pts = pts.reshape((-1, 1, 2))

img = np.zeros((200, 500, 3), np.uint8)

# Vẽ đường bao đa giác (True = khép kín)
cv.polylines(img, [pts], True, RED, 5)

# Vẽ đa giác đặc (bỏ comment dòng dưới để thử)
# cv.fillPoly(img, [pts], RED)

cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()