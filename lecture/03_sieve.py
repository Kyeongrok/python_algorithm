from math import sqrt

def sieve(n):
    ns = list(range(2, n + 1))
    check =  [True] * len(ns)

    i = 0
    while ns[i] < sqrt(n):
        if check[i] == True:
            for j in range(i + ns[i], len(ns), ns[i]): # i는 check[i]가 True일 때만 연산합니다.
                check[j] = False
        i += 1

    r = []
    for c in range(len(check)):
        if check[c]:
            r.append(ns[c])

    return r

print(sieve(100000000))


# 99999989
def is_prime(n):
    for diviser in range(2, int(sqrt(n))):# 1 2 3 4 5
        if n % diviser == 0:
            return False
    return True

# print(is_prime(99999989))
