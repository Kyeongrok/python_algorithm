from math import sqrt

def sieve(N):
    ns = list(range(2, N + 1))  # 2부터 50까지 숫자 생성
    for i in range(2, int(sqrt(N)) + 1):  # 루트 N이하의 자연수
        for j in range(len(ns) - 1, 1, -1):
            if ns[j] % i == 0 and ns[j] > i:  # 자기 자신은 지우면 안되기 때문에 > i
                ns.pop(j)
    return ns

from _datetime import datetime
print(datetime.now())
r = sieve(300_000) # 0이 5개
print(len(r))
print(datetime.now())