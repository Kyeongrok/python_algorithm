from math import sqrt
from datetime import datetime
def is_prime(n):
    for i in range(2, int(sqrt(n))): # n까지 하면 n-1까지 반복 됨
        if n % i == 0:
            return False # 한번이라도 나누어 떨어지는 수가 나오면 False
    return True # n - 1까지 나누었으나 모두 나머지가 있다면 True

# 99999989
# print(is_prime(99999989))
# print(is_prime(199999963))

print(is_prime(302036417))
