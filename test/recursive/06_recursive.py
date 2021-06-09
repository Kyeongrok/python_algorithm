import time
# while
def recursive(n):
    if n > 10: # exit condition
        return n
    else:
        return recursive(n + 1)

# result = recursive(1)
# print("=>", result)

# n! 10!
# 10 * 9 * 8 * 7 .... 2 * 1

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)

