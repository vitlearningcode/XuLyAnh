import cv2 as cv

def mouse(event, x, y, flags, param):
    # Nếu nhấn chuột trái (flags=1)
    if flags == 1:
        img[y, x] = [0, 0, 255] # Vẽ điểm đỏ
        cv.imshow('window', img)

img = cv.imread('messi.jpg')
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()