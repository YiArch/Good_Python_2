class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height


    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, win_width):
        if type(win_width) is int and win_width in range(0, 10_001):
            if win_width != self.__width:
                self.show()
            self.__width = win_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, win_height):
        if type(win_height) is int and win_height in range(0, 10_001):
            if win_height != self.__height:
                self.show()
            self.__height = win_height

# w = WindowDlg('Dlg', 123, 44)
# print(w.width, w.height)
# w.width = 200
# w.height = 300
# print(w.__dict__)
