class Stack1:
    arr = []
    last_index = 0

    def __init__(self):
        self.arr = [None] * 10000

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        temp = self.arr[self.last_index - 1]
        self.last_index -= 1
        return temp

    def is_empty(self):
        return self.last_index == 0

    def peek(self):
        return self.arr[self.last_index - 1]

st = Stack1()
st.push(10)
print(st.arr)
print(st.peek())
