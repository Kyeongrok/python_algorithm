from collections import deque
def solution(s):
    st = deque()

    for c in s:
        if len(st) == 0:
            st.append(c)
        elif st[len(st)-1] == c:
            st.pop()
        else:
            st.append(c)

    if len(st) > 0:
        return 0
    else:
        return 1


print(solution('baabaa') == 1)
print(solution('cdcd') == 0)

# programmers level2의 모든 test code통과 하는 코드