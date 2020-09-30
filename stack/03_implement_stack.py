from collections import deque
# append()
# pop()
# top()
# empty()

class Stack1():
    arr = []
    size = 0

    def __init__(self):
        self.arr = [None] * 10000

    def push(self, data):
        self.arr[self.size] = data
        self.size += 1

    def pop(self):
        if not self.empty():
            data = self.arr[self.size - 1]
            self.size -= 1
            return data
        else:
            return -1

    def top(self):
        if self.empty():
            return -1
        else:
            return self.arr[self.size - 1]

    def empty(self):
        if self.size <= 0:
            return True
        else:
            return False

st = Stack1()

st.push(100)
print(st.empty())
print(st.top())
print(st.pop())
print(st.pop())
print(st.pop())


