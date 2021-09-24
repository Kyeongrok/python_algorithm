from math import sqrt

def solution(N):
    ns = list(range(2, N+1)) #49개 0 ~ 48
    for j in range(2, int(sqrt(N)) + 1):
        for i in range(len(ns)-1, 1, -1):
            if ns[i] % j == 0 and ns[i] > j:
                ns.pop(i)
    return ns

res = solution(50)
print(len(res), res)

