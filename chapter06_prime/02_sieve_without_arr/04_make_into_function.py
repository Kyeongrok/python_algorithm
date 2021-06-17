from math import sqrt

def sieve(N):
    ns = list(range(2, N + 1)) # 2부터 N까지 숫자 생성

    for j in range(2, int(sqrt(N)) + 1): # 2의 배수부터 7의 배수까지 .pop()
        for i in range(len(ns)):
            if i >= len(ns):
                break
            if ns[i] != j and ns[i] % j == 0:
                ns.pop(i)
        print(j, ns)

    return ns


print(sieve(100))
