s = '()((()))'   # 길이 8의 문자열

while '()' in s:
    for i in range(len(s) - 1):
        if s[i] == '(' and s[i + 1] == ')':
            left = s[:i]
            right = s[i + 2:]
            s = left + right
            print('s:', s)
            break
print('s:', s)

