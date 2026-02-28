import cv2 as cv
import numpy as np

# --- ĐỊNH NGHĨA MÀU SẮC DÙNG TRONG ỨNG DỤNG ---
BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (0, 255, 255)

def help_func():
    print('--- HELP ---')
    print('Phím q: Thoát chương trình')
    print('Phím w: Tạo cửa sổ mới')
    print('Phím o: Tạo đối tượng hình khối mới')
    print('Phím t: Tạo đối tượng văn bản mới')
    print('Phím TAB: Chuyển đổi giữa các đối tượng')
    print('Phím ESC: Bỏ chọn đối tượng')
    print('Giữ ALT + Di chuột: Di chuyển đối tượng đang chọn')

class App:
    wins = []
    win = None
    win_id = 0
    options = dict(win_color=GRAY, obj_color=YELLOW, sel_color=BLUE)

    def __init__(self):
        # Thiết lập các phím tắt toàn cục
        self.shortcuts = {
            'h': help_func,
            'i': self.inspect,
            'w': Window,
            'o': Object,
            't': Text
        }
        # Khởi tạo cửa sổ đầu tiên
        Window()

    def run(self):
        help_func()
        while True:
            key = cv.waitKey(1)
            if key == ord('q'):  # Bấm 'q' để thoát vòng lặp
                break
            if key >= 0:
                k = chr(key)
                # Gửi sự kiện phím cho cửa sổ hiện tại xử lý trước
                if App.win and not App.win.key(k):
                    self.key(k)
        cv.destroyAllWindows()

    def key(self, k):
        # Nếu cửa sổ không xử lý, App sẽ xử lý các phím tắt
        if k in self.shortcuts:
            self.shortcuts[k]()

    def inspect(self):
        print('--- INSPECT ---')
        print('App.wins:', App.wins)
        print('App.win:', App.win)


class Window:
    """Class quản lý cửa sổ hiển thị"""
    obj_options = dict(pos=(20, 20), size=(100, 30), id=0)

    def __init__(self, win=None, img=None):
        App.wins.append(self)
        App.win = self
        self.objs = []
        self.obj = None
        self.upper = False

        if img is None:
            img = np.zeros((300, 600, 3), np.uint8)
            img[:, :] = App.options['win_color']

        if win is None:
            win = 'window' + str(App.win_id)
            App.win_id += 1

        self.win = win
        self.img = img
        self.img0 = img.copy()
        self.obj_options = Window.obj_options.copy()

        # Phím tắt riêng của Window
        self.shortcuts = {
            '\t': self.select_next_obj,
            chr(27): self.unselect_obj, # ESC
            chr(0): self.toggle_case,   # Các phím modifier (Ctrl/Alt/Shift)
        }

        cv.namedWindow(self.win)
        cv.imshow(self.win, self.img)
        cv.setMouseCallback(self.win, self.mouse)

    def mouse(self, event, x, y, flags, param):
        text = f'Mouse event {event} at ({x}, {y}) | Flags: {flags}'
        cv.setWindowTitle(self.win, text) # Dùng thay cho displayStatusBar

        if event == cv.EVENT_LBUTTONDOWN:
            App.win = self
            self.obj = None
            for obj in self.objs:
                obj.selected = False
                if obj.is_inside(x, y):
                    obj.selected = True
                    self.obj = obj
                    print(obj)
            self.draw()

        if event == cv.EVENT_MOUSEMOVE:
            if flags == cv.EVENT_FLAG_ALTKEY and self.obj:
                self.obj.pos = (x, y)
                self.draw()

    def draw(self):
        self.img[:] = self.img0[:]
        for obj in self.objs:
            obj.draw()
        cv.imshow(self.win, self.img)

    def key(self, k):
        if k in self.shortcuts:
            self.shortcuts[k]()
            self.draw()
            return True
        elif self.obj != None:
            self.obj.key(k)
            self.draw()
            return True
        return False

    def select_next_obj(self):
        """Chọn đối tượng tiếp theo bằng phím Tab"""
        if not self.objs: return
        try:
            i = self.objs.index(self.obj)
        except ValueError:
            i = -1
        if i != -1:
            self.objs[i].selected = False
        i = (i + 1) % len(self.objs)
        self.objs[i].selected = True
        self.obj = self.objs[i]

    def unselect_obj(self):
        if self.obj != None:
            self.obj.selected = False
            self.obj = None

    def toggle_case(self):
        self.upper = not self.upper
        state = 'UPPER case' if self.upper else 'LOWER case'
        cv.setWindowTitle(self.win, state)


class Object:
    """Class cơ sở cho các đối tượng vẽ lên màn hình"""
    def __init__(self, **options):
        if App.win is None: return
        App.win.objs.append(self)
        App.win.obj = self
        self.img = App.win.img
        self.selected = False

        d = App.win.obj_options
        d.update(options)

        self.id = d['id']
        self.pos = x, y = d['pos']
        self.size = w, h = d['size']

        d['id'] += 1
        d['pos'] = x, y + h + 5 # Tự động dời xuống cho object tiếp theo

    def __str__(self):
        return 'Object {} at ({}, {})'.format(self.id, self.pos[0], self.pos[1])

    def is_inside(self, x, y):
        x0, y0 = self.pos
        w, h = self.size # Sách in sai là w, h = self.pos, đã sửa lại
        return x0 <= x <= x0 + w and y0 <= y <= y0 + h

    def draw(self):
        x, y = self.pos
        w, h = self.size
        # Sửa cấu trúc tọa độ cho phù hợp với OpenCV bản mới
        cv.rectangle(self.img, (x, y), (x+w, y+h), App.options['obj_color'], 1)
        if self.selected:
            cv.rectangle(self.img, (x-2, y-2), (x+w+2, y+h+2), App.options['sel_color'], 2)

    def key(self, k):
        pass


class Text(Object):
    """Class hiển thị và chỉnh sửa văn bản (kế thừa từ Object)"""
    options = dict(
        fontFace=cv.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=BLUE,
        thickness=2,
        lineType=cv.LINE_AA,
    )

    def __init__(self, text='Text', **options):
        self.text_options = Text.options.copy()
        for k, v in options.items():
            if k in self.text_options:
                self.text_options[k] = v
        super().__init__(**options)
        self.text = text
        self.update_size()

    def get_size(self):
        d = self.text_options
        size, baseline = cv.getTextSize(self.text, d['fontFace'], d['fontScale'], d['thickness'])
        return size, baseline

    def update_size(self):
        size, baseline = self.get_size()
        # Thêm khoảng đệm (padding) cho khung chữ nhật
        self.size = (size[0] + 10, size[1] + 10)

    def draw(self):
        super().draw()
        d = self.text_options
        x, y = self.pos
        size, baseline = self.get_size()
        # Chữ trong OpenCV tính từ góc dưới bên trái (baseline)
        cv.putText(self.img, self.text, (x + 5, y + size[1] + 5), 
                   d['fontFace'], d['fontScale'], d['color'], d['thickness'], d['lineType'])

    def key(self, k):
        # Hỗ trợ xóa chữ bằng Backspace
        if k == '\b' or ord(k) == 8: 
            self.text = self.text[:-1]
        elif k == '\r' or k == '\n':
            pass
        else:
            if App.win.upper:
                k = k.upper()
            self.text += k
        self.update_size()


class Node:
    """Class cho cấu trúc dữ liệu phân cấp (Hierarchical Tree)"""
    options = dict(
        pos=np.array((20, 20)),
        size=np.array((100, 40)),
        gap=np.array((10, 10)),
        dir=np.array((0, 1)),
    )

    def __init__(self, parent=None, **options):
        for k, v in options.items():
            if k in Node.options:
                if isinstance(v, tuple):
                    v = np.array(v)
                Node.options[k] = v

        self.pos = None
        self.size = None
        self.gap = None
        self.dir = None
        self.__dict__.update(Node.options)
        
        self.parent = parent
        self.children = []
        self.selected = False

        if parent:
            parent.children.append(self)
            self.img = parent.img
        elif App.win:
            self.img = App.win.img
        else:
            self.img = None

        pos = self.pos + (self.size + self.gap) * self.dir
        Node.options['pos'] = pos

    def draw(self, pos=np.array((0, 0))):
        if self.img is None: return
        x, y = pos + self.pos
        w, h = self.size
        cv.rectangle(self.img, (x, y), (x+w, y+h), RED, 1)
        if self.selected:
            cv.rectangle(self.img, (x-2, y-2), (x+w+4, y+h+4), GREEN, 1)
        
        for child in self.children:
            child.draw(pos + self.pos)

    def is_inside(self, pos):
        pos = np.array(pos)
        return all(self.pos <= pos) and all(pos <= self.pos + self.size)

    def enclose_children(self):
        p = np.array((0, 0))
        for node in self.children:
            p = np.maximum(p, node.pos + node.size)
        self.size = p


if __name__ == '__main__':
    # Chạy vòng lặp ứng dụng
    App().run()