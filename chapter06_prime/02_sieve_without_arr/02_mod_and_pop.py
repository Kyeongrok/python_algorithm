N = 50
ns = list(range(2, N + 1)) # 2부터 50까지 숫자 생성

j = 2
while j * j < N:
    for i in range(j, len(ns)):
        if i >= len(ns):
            break
        if ns[i] % j == 0:
            ns.pop(i)
    j += 1

print(len(ns), ns)