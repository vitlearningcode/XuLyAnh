import cv2 as cv

img = cv.imread('messi.jpg')
cv.imshow('window', img)

# Lưu ảnh gốc dưới định dạng png
cv.imwrite('messi.png', img)

# Chuyển sang ảnh xám và lưu
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('messi_gray.png', gray)

cv.waitKey(0)
cv.destroyAllWindows()