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

s = '(' * 5_000_000 + ')'*5_000_000
start_time = datetime.now()
print(f's_cnt:{len(s)} result:{solution(s)}')
print(datetime.now() - start_time)
