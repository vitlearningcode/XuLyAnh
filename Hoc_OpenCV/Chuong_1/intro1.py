import cv2 as cv

# Đọc ảnh (đảm bảo file messi.jpg có trong thư mục)
img = cv.imread('messi.jpg')

# Hiển thị ảnh trong cửa sổ tên là 'window'
cv.imshow('window', img)

# Chờ nhấn phím bất kỳ để đóng (0 nghĩa là chờ vô hạn)
cv.waitKey(0)
cv.destroyAllWindows()