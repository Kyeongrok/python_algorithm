N = 50
ns = list(range(2, N + 1))
check = [True] * len(ns)

i = 0
while ns[i] * ns[i] <= N:
    if check[i]:
        for j in range(2, len(ns), 2):
            check[j] = False
            print(ns[i], ns[j])
    i += 1
