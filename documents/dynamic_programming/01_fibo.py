# fibo with memoization
# array에 중간 결과를 저장한다.
# 중간 결과는 parameter로 recursive 구간을 돌아다닌다.

def fibo(n, lookup):
    # 처음
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]

lookup = [None] * 101
print(fibo(5, []))