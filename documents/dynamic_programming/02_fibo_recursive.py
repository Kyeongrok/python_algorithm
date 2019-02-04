# fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3
def fib(n, lookup):
    # 처음
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]

lookup = [None] * 101
print(fib(6, lookup))
