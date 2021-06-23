N = 121
ns = list(range(2, N + 1))
check = [True] * len(ns)

j = 0
while ns[j] * ns[j] <= N:
    print(j, ns[j])
    j += 1

