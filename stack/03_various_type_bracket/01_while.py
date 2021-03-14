s = '({([])})'
while '()' in s or '{}' in s or '[]' in s:
    sp = s.split('()')
    s = ''.join(sp)
    sp = s.split('{}')
    s = ''.join(sp)
    sp = s.split('[]')
    s = ''.join(sp)
    print(s)

print(len(s) == 0)
