class StackObj:
    def __init__(self, data):
        self.__next = None
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
            self.top.next = None
        else:
            last = self.top
            while True:
                if last.next is None:
                    obj.next = None
                    last.next = obj
                    break
                last = last.next

    def pop(self):
        if self.top is None:
            return None
        current = self.top
        previous = self.top
        while current is not None:
            if current.next is None:
                res = current
                previous.next = None
                if current == self.top:
                    self.top = None
                return res
            previous = current
            current = current.next

    def get_data(self):
        data_lst = []
        next_obj = self.top
        while next_obj is not None:
            data_lst.append(next_obj.data)
            next_obj = next_obj.next
        return data_lst

# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()
# print(res)
# st = Stack()
# print(st.get_data())
# print(st.pop())