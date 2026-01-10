import cv2 as cv

def mouse(event, x, y, flags, param):
    text = f'mouse at ({x}, {y}), flags={flags}, param={param}'
    try:
        cv.displayStatusBar('window', text, 1000) # displayStatusBar cũng yêu cầu Qt
    except:
        print(text)

img = cv.imread('messi.jpg')
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()