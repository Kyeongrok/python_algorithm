class Stack1():
    arr = []  # 스텍은 배열을 확장한 기능으로 배열을 선언해줍니다.

    def __init__(self, size=10000):
        self.st = [None] * size

    def push(self, value):
        self.arr.append(value)

    # 뒤에서 뽑는 기능

st = Stack1()
st.push(15)
print(st.arr)