s = '()((()))'   # 길이 8의 문자열

while '()' in s:
    sp = s.split('()')
    print(sp)
    s = ''.join(sp)
    print('s:', s)
print('final s:', s)

