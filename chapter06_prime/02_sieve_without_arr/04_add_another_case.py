from math import sqrt

N = 50
ns = list(range(2, N + 1)) # 2부터 50까지 숫자 생성

for i in range(2, int(sqrt(N)) + 1): # 루트 N이하의 자연수
    for j in range(len(ns) - 1, 1, -1):
        if ns[j] % i == 0 and ns[j] > i: # 자기 자신은 지우면 안되기 때문에 > i
            ns.pop(j)
    print(i, len(ns), ns)