from st1 import Stack1
from datetime import datetime

def solution(s):
    st = Stack1(len(s))
    for i in range(len(s)):
        if s[i] == '(':
            st.push(s[i])
        elif s[i] == ')':
            if st.empty():
                return False
            st.pop()
    return st.empty()

s = '(' * 5000000 + ')'*5000000
print(datetime.now())
print('result:', solution(s))
print(datetime.now())
