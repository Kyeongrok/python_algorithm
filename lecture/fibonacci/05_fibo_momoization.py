def fib(n, lookup):
    if n <= 1:
        return n

    # lookup[n]이 없을때 None일때 계산해서 넣는 로직
    if lookup[n] is None:
        lookup[n] = fib(n-2, lookup) + fib(n-1, lookup)

    return lookup[n]

n = 100
lookup = [None] * (n + 1)
print(lookup)
print(fib(n, lookup))