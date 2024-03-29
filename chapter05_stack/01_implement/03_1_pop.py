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
st.push(15)
st.push(20)
print(st.arr[:10])
print(st.pop())
print(st.arr[:10])
st.push(30)
print(st.arr[:10])


total = 30
gsp = 4
td = 2.8 * 6

print(td)
