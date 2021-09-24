s = '()((()))'   # 길이 8의 문자열

for i in range(len(s) - 1):
    if s[i] == '(' and s[i+1] == ')':
        print(i, i + 1, '(', ')')
