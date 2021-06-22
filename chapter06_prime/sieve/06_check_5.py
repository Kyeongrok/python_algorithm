n = 50
ns = list(range(2, n + 1))
check = [True] * len(ns)

for i in range(2, len(ns), 2):
    check[i] = False

for i in range(4, len(ns), 3):
    check[i] = False

res = []
for i in range(len(check)):
    if check[i]:
        res.append(ns[i])

print(len(res), res)

from math import sqrt

print(sqrt(123))