# think reverse it can give you a key

# 0 1 2 3 4 5 6
# 1 1 2 3 5 8 13

# receive index
# fib(4) = 5
# fib(1) = 1

def fib(n):
    if n < 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

for i in range(10):
    print(fib(i))
