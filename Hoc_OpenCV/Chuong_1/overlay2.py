# overlay2.py - Hiển thị chi tiết thông tin ảnh
import cv2 as cv

file = 'messi.jpg'
img = cv.imread(file, cv.IMREAD_COLOR)
cv.imshow('window', img)

text = f'file name: {file}\nwidth: {img.shape[1]}\nheight: {img.shape[0]}\nchannels: {img.shape[2]}'
try:
    cv.displayOverlay('window', text)
except:
    print(text)

cv.waitKey(0)
cv.destroyAllWindows()