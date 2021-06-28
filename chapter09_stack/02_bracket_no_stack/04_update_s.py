s = '()((()))'   # 길이 8의 문자열

for i in range(len(s) - 1):
    if s[i] == '(' and s[i + 1] == ')':
        left = s[:i]
        right = s[i + 2:]
        s = left + right
        print('left:', left)
        print('right:', right)
        print('s:', s)

