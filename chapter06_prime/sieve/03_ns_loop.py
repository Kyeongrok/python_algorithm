N = 50
ns = list(range(2, N + 1))
check = [True] * len(ns)

i = 0
while ns[i] * ns[i] <= N:
    for j in range(len(ns)):
        if ns[j] % ns[i] == 0:
            check[j] = False
        print(ns[i], ns[j], ns[j] % ns[i] == 0)
    i += 1

print(check)