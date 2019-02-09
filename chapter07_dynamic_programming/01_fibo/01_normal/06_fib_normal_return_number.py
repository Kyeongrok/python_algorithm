def fib(n):
    # 1, 1, 2, 3, 5, 8
    result = []

    first = 1
    second = 1
    third = 2

    result.append(first)
    result.append(second)
    for i in range(2, n):
        third = first + second
        result.append(third)
        first = second
        second = third

    return result.pop()

print(fib(100))
