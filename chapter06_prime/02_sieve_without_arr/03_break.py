N = 50
ns = list(range(2, N + 1)) # 2부터 50까지 숫자 생성

for j in range(2, 7 + 1): # 2의 배수부터 7의 배수까지 .pop()
    for i in range(len(ns)):
        if i >= len(ns):
            break
        if ns[i] % j == 0:
            ns.pop(i)

print(ns)