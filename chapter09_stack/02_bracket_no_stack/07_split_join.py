s = '()((()))'   # 길이 8의 문자열

while '()' in s:
    for i in range(len(s) - 1):
        if s[i] == '(' and s[i + 1] == ')':
            sp = s.split('()')
            s = ''.join(sp)
            print('s:', s)
            break
print('final s:', s)

