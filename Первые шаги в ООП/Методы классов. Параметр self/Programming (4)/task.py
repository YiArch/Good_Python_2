class Translator:

    en_ru_dict = {}

    def add(self, eng, rus):
        self.en_ru_dict.setdefault(eng, []).append(rus)

    def remove(self, eng):
        del self.en_ru_dict[eng]

    def translate(self, eng):
        res = self.en_ru_dict[eng]
        return res


tr = Translator()

in_str = '''tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко'''

for item in in_str.split('\n'):
    en_w, ru_w = item.split(' - ')
    tr.add(en_w, ru_w)

tr.remove('car')
print(*tr.translate('go'))
