from st1 import Stack1

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

s = '()((()))'   # 길이 8의 문자열
s = ')((()))'   # 길이 7의 문자열
s = '(' * 5000000 + ')'*5000000
print('result:', solution(s))
