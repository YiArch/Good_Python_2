class ObjList:
    def __init__(self, data):
        self.__next = self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head, self.tail = None, None

    def add_obj(self, obj):
        if not self.tail:
            obj.set_prev = None
            self.head = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
        self.tail = obj

    def remove_obj(self):
        if not self.tail:
            prev = self.tail.get_prev()
            if prev:
                prev.set_next(None)
            self.tail = prev
            if not self.tail:
                self.head = None

    def get_data(self):
        data_lst = []
        head = self.head
        while head:
            data_lst.append(head.get_data())
            head = head.get_next()
        return data_lst
