from datetime import datetime

def solution(s):
   open_bracket_cnt = 0 # 스택 대신 변수를 선언 합니다.
   for i in range(len(s)):
       if s[i] == '(':
           open_bracket_cnt += 1
       elif s[i] == ')':
           if open_bracket_cnt == 0:
               return False
           open_bracket_cnt -=1  # .pop()을 하는 대신 개수를 줄여줍니다.
   return open_bracket_cnt == 0

s = '(' * 5000000 + ')'*5000000
print(datetime.now())
print('result:', solution(s))
print(datetime.now())