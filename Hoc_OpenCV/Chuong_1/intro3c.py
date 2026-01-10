import cv2 as cv

img = cv.imread('messi.jpg')

# Tô màu xanh cho vùng ảnh
img[250:300, 50:550] = (0, 255, 0)

# Cắt vùng khuôn mặt (tọa độ ước lượng cho ảnh messi.jpg chuẩn)
face = img[80:230, 270:390]

# Dán vùng mặt vào góc trái trên
img[0:150, 0:120] = face

cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()