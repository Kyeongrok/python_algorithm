s = '()((()))'   # 길이 8의 문자열

for i in range(len(s)):
    if s[i] == '(':
        print(s[i], '여는 괄호')
    elif s[i] == ')':
        print(s[i], '닫는 괄호')


