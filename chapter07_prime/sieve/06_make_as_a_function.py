def sieve(N):
    ns = list(range(2, N + 1))
    check = [True] * len(ns)

    i = 0
    while ns[i] * ns[i] <= N:
        if check[i]:
            for j in range(ns[i] + i, len(ns), ns[i]):
                check[j] = False
        i += 1

    primes = []
    for i in range(len(check)):
        primes.append(ns[i])
    return primes

from datetime import datetime

start_time = datetime.now()
N = 10000000
res = sieve(N)
end_time = datetime.now()
print(len(res), max(res))
print(end_time - start_time)
