from _collections import deque

def is_pair(open_bracket, close_bracket):
    if open_bracket == '(' and close_bracket == ')':
        return True
    elif open_bracket == '{' and close_bracket == '}':
        return True
    elif open_bracket == '[' and close_bracket == ']':
        return True
    else:
        return False

def solution(str):
    # 닫는 괄호가 아니면 stack에 넣는다
    # 닫는 괄호가 나오면 짝이 나올때까지 뽑는다.
    # (((})()()))
    st = deque()
    for c in str:
        if c == '(' or c == '{' or c == '[':
            st.append(c)
        else:
            if len(st) == 0:
                return False
            elif is_pair(st[-1], c):
                st.pop()
            else:
                return False

    if len(st) == 0:
        return True
    else:
        return False
print(solution('(') == False)
print(solution(')') == False)
print(solution('(())') == True)
print(solution('(()') == False)
print(solution('(()}') == False)
print(solution('{()}') == True)
print(solution('(()}') == False)
print(solution('((){})') == True)
