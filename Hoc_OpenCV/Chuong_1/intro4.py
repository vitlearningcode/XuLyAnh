import cv2 as cv

class Window:
    def __init__(self, win, img):
        self.win = win
        self.img = img
        cv.imshow(win, img)

class App:
    def __init__(self):
        img = cv.imread('messi.jpg')
        if img is None:
            print("Không tìm thấy ảnh messi.jpg")
            return
        Window('image', img)
    
    def run(self):
        k = 0
        while k != ord('q'):
            k = cv.waitKey(0)
            print(k, chr(k) if k < 256 else '?')
        cv.destroyAllWindows()

if __name__ == '__main__':
    App().run()