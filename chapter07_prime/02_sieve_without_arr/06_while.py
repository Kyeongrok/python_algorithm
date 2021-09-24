def sieve(N):
    ns = list(range(2, N + 1))  # 2부터 50까지 숫자 생성
    i = 0
    while ns[i] * ns[i] <= N:
        for j in range(len(ns) - 1, 1, -1):
            # 자기 자신은 지우면 안되기 때문에 > ns[i]
            if ns[j] % ns[i] == 0 and ns[j] > ns[i]:
                ns.pop(j)
        i += 1
    return ns

from _datetime import datetime
print(datetime.now())
r = sieve(300_000) # 0이 5개
print(len(r))
print(datetime.now())