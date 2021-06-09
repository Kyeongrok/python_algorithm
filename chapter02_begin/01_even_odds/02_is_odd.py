# 입력 받은 숫자가 홀수인지
def is_odd(number):
    return number % 2 != 0

print(is_odd(3))
print(is_odd(7))
print(is_odd(10))

is_odd_lam = lambda x: x % 2 != 0

print(is_odd_lam(10))
print(is_odd_lam(11))
