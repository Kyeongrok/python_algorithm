from math import sqrt

n = 100
ns = list(range(2, n + 1))

for i in range(2, int(sqrt(n)) + 1):
    print(i, len(ns), ns)
    for j in range(i, len(ns)):
        if j >= len(ns):
            break

        if ns[j] % i == 0:
            ns.pop(j)

print(ns)

