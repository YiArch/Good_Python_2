class FloatValue:
    @classmethod
    def is_float(cls, num):
        if type(num) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.is_float(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.m = m
        self.n = n
        self.cells = [[Cell(0.0) for _ in range(self.m)] for _ in range(self.n)]


table = TableSheet(5, 3)
for r in range(5):
    for c in range(3):
        table.cells[r][c].value = r * 3 + c + 1.0

