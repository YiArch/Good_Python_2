import sys

class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj

# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

head_obj = ListObject(lst_in[0])
prev_obj = head_obj
for row in lst_in[1:]:
    next_obj = ListObject(row)
    prev_obj.link(next_obj)
    prev_obj = next_obj


