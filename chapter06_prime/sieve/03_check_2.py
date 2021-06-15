n = 50
ns = list(range(2, n + 1))
check = [True] * len(ns)

for i in range(2, len(ns), 2): # 세번째 파라메터 중요
    check[i] = False

print(len(ns), ns)
print(check)
