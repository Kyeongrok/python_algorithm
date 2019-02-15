# fib(1) = 1, fib(2) = 1 , fib(3) = 2, fib(4) = 3
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2) # fib(2) = fib(1) + fib(0)

print(fib(40))
