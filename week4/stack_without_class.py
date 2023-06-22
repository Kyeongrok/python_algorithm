
class Stack:
    arr = [None] * 1000
    last_index = 0

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def is_empty(self):
        return self.last_index == 0

    def pop(self):
        if not self.is_empty():
            temp = self.arr[self.last_index - 1] # -1
            self.last_index -= 1
            return temp
        else:
            raise Exception("스택이 비어있습니다.")

    def peek(self):
        if not self.is_empty():
            return self.arr[self.last_index - 1]
        else:
            raise Exception("스택이 비어있습니다.")

st = Stack()
print(st.is_empty())
st.push(10)
print(st.is_empty())
st.push(20)
print(st.peek())
st.pop()
st.pop()
print(st.peek())


