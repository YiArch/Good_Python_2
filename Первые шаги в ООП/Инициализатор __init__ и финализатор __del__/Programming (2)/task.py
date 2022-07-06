from random import choice, randint as ri

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = [choice([Line, Rect, Ellipse])(ri(0, 100), ri(0, 100), ri(0, 100), ri(0, 100)) for _ in range(217)]
for elem in elements:
    if isinstance(elem, Line):
        elem.sp = (0, 0)
        elem.ep = (0, 0)
# figs = [Line, Rect, Ellipse]
# elements = []
# for i in range(217):
#     meth = choice(figs)
#     if meth == Line:
#         elements.append(Line(0, 0, 0, 0))
#     else:
#         a, b, c, d = randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)
#         elements.append(meth(a, b, c, d))