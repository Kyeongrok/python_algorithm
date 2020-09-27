# '<open>hello<close>' -> '<open>olleh<close>'
# 'abb<open>hello<close>' -> 'bba<open>olleh<close>'

from collections import deque

def solution(string):
    answer = ''
    d = deque()
    is_tag = False

    for c in string:
        if c == '<':
            while len(d) > 0:
                answer += d.pop()
            answer += c
            is_tag = True
        elif c == '>':
            answer += c
            is_tag = False
        elif is_tag:
            answer += c
        else:
            if c == ' ':
                while len(d) > 0:
                    answer += d.pop()
                answer += c
            else:
                d.append(c)
    return answer

print(solution('<open>hello world<close>') == '<open>olleh dlrow<close>')
print(solution('ab<open>hello<close>') == 'ba<open>olleh<close>')
