from datetime import datetime

def solution(s):
    open_bracket_cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            open_bracket_cnt += 1
        elif s[i] == ')':
            if open_bracket_cnt == 0:
                return False
            open_bracket_cnt -=1
    return open_bracket_cnt == 0

s = '(' * 5000000 + ')'*5000000
print(datetime.now())
print('result:', solution(s))
print(datetime.now())
