from _collections import deque

def solution(string):
    st = deque()

    for i in range(len(string)):
        # (면 넣고
        # )면 (가 나올때까지 pop()
        # (()), (()()), ),
        if string[i] == '(':
            st.append(string[i])
        elif string[i] == ')':
            if len(st) == 0:
                return False
            elif len(st) > 0 and st[-1] == '(':
                st.pop()
            else:
                print(f"{st}, {string[i]}, {i}")
    return len(st) == 0

print(solution('()'))
print(solution('(())'))
print(solution('()()'))
print(solution('(()())'))
print(solution(')'))
print(solution('((())'))

