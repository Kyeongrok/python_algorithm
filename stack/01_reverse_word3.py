from _collections import deque

def solution(string):
    st = deque()
    string += '\n'
    result = ''
    for c in string:
        if c != ' ' and c != '\n':
            st.append(c)
        else:
            while len(st) > 0:
                result += st.pop()
            if c == ' ':
                result += ' '
    return result
print(solution('hello world krk') == 'olleh dlrow krk')
