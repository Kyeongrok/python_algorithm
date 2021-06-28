class Stack1():
    arr = []
    last_index = 0

    def __init__(self, size=10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        value = self.arr[self.last_index - 1]
        self.last_index -= 1
        return value

st = Stack1()
print(st.pop())

from _collections import deque

[].pop()

