N = 50
ns = list(range(2, N + 1))
check = [True] * len(ns)

i = 0
while ns[i] * ns[i] <= N:
    if check[i]:
        print(i, ns[i], check[i])
    i += 1
