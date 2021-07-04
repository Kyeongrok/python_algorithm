from st1 import Stack1
from datetime import datetime

def is_pair(first, second):
    if first == '(' and second == ')':
        return True
    elif first == '{' and second == '}':
        return True
    elif first == '[' and second == ']':
        return True
    return False

def solution(s):
    st = Stack1(len(s))
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.push(s[i])
        elif is_pair(st.peek(), s[i]):
            if st.empty():
                return False
            st.pop()
    return st.empty()

s = ')((()))'   # 길이 7의 문자열
s = '{}(([]))'   # 길이 8의 문자열
s = '()((()))'   # 길이 8의 문자열
s = '(' * 2000000 + ')'*2000000

s = f'{"("*(2*pow(10,4))}{"{"*(2*pow(10,4))}{"["*(2*pow(10,4))}{"]"*(2*pow(10,4))}{"}"*(2*pow(10,4))}{")"*(2*pow(10,4))}'
start_time = datetime.now()
print('result:', solution(s))
print(datetime.now() - start_time)
