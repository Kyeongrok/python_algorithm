def solution(name):
    answer = 0
    init = 'A'*len(name)

    answer += len(name) - 1
    for i in range(len(name)):
        diff = ord(name[i]) - ord(init[i])
        answer += min(diff, 26 - diff)

    cnt_a = 0
    for j in range(1, len(name)):
        if name[j] == 'A':
            cnt_a += 1
        else:
            break
    answer -= cnt_a

    return answer

print(solution('JEROEN') == 56)
print(solution('JZ') == 11)
print(solution('JAN') == 23)
print(solution('J') == 9)
print(solution('A') == 0)
print(solution('B') == 1)
print(solution('BAZ') == 3)
print(solution('BAAZ') == 3)
print(solution('BAAAAAZ') == 3)
print(solution('BAAAAA') == 1)
print(solution('AAAAA') == 0)
print(solution('AAAAAZ') == 2)
print(solution('AAAAAZA') == 3)
print(solution('ABABAAAAABA') == 11)