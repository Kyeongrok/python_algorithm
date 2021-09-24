class Stack1():
    arr = []
    last_index = 0

    def __init__(self, size=10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        if self.last_index <= 0: # self.last_index가 0이하라면
            raise Exception('Stack is empty')

        value = self.arr[self.last_index - 1]
        self.last_index -= 1
        return value


st = Stack1()
print(st.pop()) # self.last_index가 0인 상태에서 .pop()수행
st.push(40)
print(st.arr[:10])     # 앞에서 10개 출력

