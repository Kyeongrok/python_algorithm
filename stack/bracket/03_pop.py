from st1 import Stack1

s = '()((()))'   # 길이 8의 문자열
st = Stack1(len(s))
for i in range(len(s)):
    if s[i] == '(':
        print(s[i], '여는 괄호 st.push()')
        st.push(s[i])
    elif s[i] == ')':
        print(s[i], '닫는 괄호')

print(st.arr)
