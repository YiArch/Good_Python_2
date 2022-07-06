class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show


    def dec(func):
        def wrapper(self):
            if self.is_show:
                return func(self)
            else:
                print('Отображение данных закрыто')
        return wrapper


    def set_data(self, data):
        self.data = data


    @dec
    def show_table(self):
        return ' '.join(map(str, self.data))


    @dec
    def show_graph(self):
        print('Графическое отображение данных:', self.show_table())


    @dec
    def show_bar(self):
        print('Столбчатая диаграмма:', self.show_table())


    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
