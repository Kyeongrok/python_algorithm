def solution(s):
    st = []  # 스텍 역할을 할 list 생성하기
    for i in range(len(s)):
        if s[i] == '(':   # (여는 괄호일때의 조건문 추가
            print('여는 괄호')
        elif s[i] == ')': # ) 닫는 괄호일때의 조건문 추가
            print('닫는 괄호')

print(solution("()()"))
