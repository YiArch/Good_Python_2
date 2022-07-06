class RadiusVector2D:
    MIN_COORD, MAX_COORD = -100, 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.check_number(x):
            self.__x = x
        if self.check_number(y):
            self.__y = y

    def check_number(self, num):
        return type(num) in (int, float) and self.MIN_COORD <= num <= self.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, var_x):
        if self.check_number(var_x):
            self.__x = var_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, var_y):
        if self.check_number(var_y):
            self.__y = var_y

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2

# r1 = RadiusVector2D(0, 0)
# print(r1.__dict__)