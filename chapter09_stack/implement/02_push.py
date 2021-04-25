class Stack1():
    arr = []
    last_index = 0

    def __init__(self, size=10000):
        self.arr = [None] * size

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1


st = Stack1()
st.push(15)
st.push(20)
print(st.arr)