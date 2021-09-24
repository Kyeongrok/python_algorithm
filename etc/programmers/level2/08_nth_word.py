def solution(n, t, m, p):
    answer = ''
    cnt = 0

    for i in range(t):
        for j in range(n):
            if i + 1 % p == 0:
                print(j)


    return answer


# print(solution(2,4,2,1))
print(solution(16,16,2,2))
