from st1 import Stack1

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
s = f'{"("*(2*pow(10,7))}{"{"*(2*pow(10,7))}{"["*(2*pow(10,7))}{"]"*(2*pow(10,7))}{"}"*(2*pow(10,7))}{")"*(2*pow(10,7))}'
print(len(s))
print('result:', solution(s))
