import cv2 as cv

img = cv.imread('fish.jpg')
cv.imshow('window', img)

while True:
    k = cv.waitKey(0) & 0xFF
    if k == ord('q'): # Nhấn 'q' để thoát
        break
    elif k == ord('v'):
        img = cv.flip(img, 0) # Lật dọc (trục x)
    elif k == ord('h'):
        img = cv.flip(img, 1) # Lật ngang (trục y)
    
    cv.imshow('window', img)

cv.destroyAllWindows()