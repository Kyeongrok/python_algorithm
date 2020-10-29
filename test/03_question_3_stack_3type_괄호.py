from collections import deque

def solution(s):
    st = deque()
    for ch in s:
        # 닫는 bracket이 나올 때 까지 stack에 append한다
        # 닫는 bracket이 나오면 pop한다. 하지만 같은 종류의 brack이어야 한다.
        '''
        [(]
        '''
        if ch != ")" and ch != "}" and ch != "]":
            st.append(ch)
        elif ch == ")" or ch == '}' or ch == ']':
            if len(st) == 0:
                return False
            if ch == ')':
                while len(st) > 0 and st[-1] == '(':
                    st.pop()
            if ch == '}':
                while len(st) > 0 and st[-1] == '{':
                    st.pop()
            if ch == ']':
                while len(st) > 0 and st[-1] == '[':
                    st.pop()
    return len(st) == 0

'''
[((]
'''
print(solution("()[]{}") == True)
print(solution(")[]{}") == False)
print(solution("(]") == False)
print(solution("([)]") == False)
print(solution("{[]}") == True)
print(solution("((((") == True)
print(solution("))))") == True)
print(solution("))})])") == True)
