import cv2 as cv

def trackbar(x):
    text = f'Trackbar: {x}'
    try:
        cv.displayOverlay('window', text, 1000)
    except:
        print(text)
    cv.imshow('window', img)

img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
cv.imshow('window', img)

# Tạo thanh trượt tên 'x', giá trị từ 0-255, giá trị đầu 100
cv.createTrackbar('x', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()