def fib(n, lookup):

    for i in range(1, n):
        fib(n - 2, lookup) + fib(n + 1, lookup)
    return lookup[n]

lookup = [] * 6
print(lookup)
print(fib(6, lookup))