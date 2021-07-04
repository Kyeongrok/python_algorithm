def solution(s):
    while '()' in s:
        sp = s.split('()')
        s = ''.join(sp)
    return len(s) == 0

s = '()((()))'   # 길이 8의 문자열
print('result:', solution(s))
