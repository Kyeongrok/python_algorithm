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

    def empty(self):
        if self.last_index == 0:
            return True
        else:
            return False

    def peek(self):
        if self.empty():
            raise Exception('Stack is Empty.')
        return self.arr[self.last_index - 1]


s = '()((()))'   # 길이 8의 문자열
st = Stack1(len(s))
for i in range(len(s)):
    if s[i] == '(':
        print(s[i], '여는 괄호 st.push()')
        st.push(s[i])
    elif s[i] == ')':
        print(s[i], '닫는 괄호')

print(st.arr)