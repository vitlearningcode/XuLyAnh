# overlay.py
import cv2 as cv

file = 'messi.jpg'
img = cv.imread(file, cv.IMREAD_COLOR)
cv.imshow('window', img)

# Hiển thị overlay (chỉ hoạt động với Qt backend)
try:
    cv.displayOverlay('window', f'file name: {file}')
except:
    print(f"Overlay text: file name: {file}")

cv.waitKey(0)
cv.destroyAllWindows()
