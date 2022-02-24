class Stack1:
    last_index = 0
    arr = []

    def __init__(self, n):
        self.arr = [None] * n

    def push(self, value):
        self.arr[self.last_index] = value
        self.last_index += 1

    def pop(self):
        if self.last_index == 0:
            raise Exception("Stack is Empty.")
        value = self.arr[self.last_index - 1]
        self.last_index -= 1
        return value

    def empty(self):
        return self.last_index == 0

def solution(b):
    st = Stack1(len(b))
    for i in range(len(b)):
        if b[i] == '(':
            st.push(b[i])
        elif b[i] == ')':
            if st.empty():
                return False
            st.pop()
    return st.empty()

print(solution('()((()))'))
print(solution('()((())))'))
