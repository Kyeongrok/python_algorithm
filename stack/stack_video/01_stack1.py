class Stack1:
    def __init__(self, size=10000):
        self.arr = [None] * size
        self.last_index = 0 # 현재 사용할 수 있는 인덱스

    def push(self, value):
        # self.arr = [None, None, None, None, None, None, None,
        # self.last_index = 0
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        # 뒤(위)에서 뽑기
        # last_index = 0 ---> -1
        if self.empty():
            raise Exception('Stack is empty.')
        self.last_index = self.last_index - 1
        return self.arr[self.last_index]

    def empty(self):
        if self.last_index == 0:
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            raise Exception('Stack is empty')
        return self.arr[self.last_index - 1]

st = Stack1(100)
st.push(20)
print(st.peek())
