def fib(n, lookup):
    if n <= 1:
        return n
    return fib(n-2, lookup) + fib(n-1, lookup)

lookup = []
print(fib(60, lookup))