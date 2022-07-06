class SingletonFive:

    __count = 0
    __addr = None

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        if cls.__count < 6:
            cls.__addr = super().__new__(cls)
        return cls.__addr

    def __init__(self, name):
        self.name = name



objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять