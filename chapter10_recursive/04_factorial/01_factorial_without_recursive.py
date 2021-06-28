def factorial(n):
    result = 1

    for i in range(n, 0, -1):
        print(i)
        result *= i
    return result

print(factorial(4))