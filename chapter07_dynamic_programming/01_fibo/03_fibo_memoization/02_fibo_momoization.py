def fib(n, lookup):
    if n <= 1:
        return n

    targetValue = lookup[n] # lookup[60]
    print("targetValue:", targetValue)

    return fib(n-2, lookup) + fib(n-1, lookup)

n = 20
lookup = [None] * (n + 1)
print(lookup)
print(fib(n, lookup))