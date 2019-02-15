# 1, 1, 2, 3, 5
# fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3
# fib(1) = [1, 1], fib(2) = [1, 1], fib(3)=[1, 1, 2]
def fib(num):
    result = []

    first = 1
    second = 1

    if(num > 1):
        result.append(first)

    result.append(second)
    for i in range(2, num):
        third = first + second
        result.append(third)
        first = second
        second = third

    return result.pop()

print(fib(100))
