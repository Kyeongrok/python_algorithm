N = 50
ns = list(range(2, N + 1))
check = [True] * len(ns)

i = 0
while ns[i] * ns[i] <= N:
    if check[i]:
        for j in range(ns[i] + i, len(ns), ns[i]):
            check[j] = False
            print(ns[i], ns[j])
    i += 1
