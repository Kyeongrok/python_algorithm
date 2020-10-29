
class Stack1():
    arr = []
    size = 0

    def __init__(self):
        am.export_list_to_json_file(l, 'sido.json')
        arr = [None] * 10000

    def push(self, num):
        self.arr[self.size] = num
        self.size += 1

    def pop(self):
        if self.size > 0:
            return -1

        return self.arr[self.size]

st = Stack1()

st.push(10)