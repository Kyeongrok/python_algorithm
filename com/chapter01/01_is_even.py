# 입력 받은 숫자가 짝수인지
def is_even(number):
    return number % 2 == 0

print(is_even(3))
print(is_even(7))
print(is_even(10))

is_even_lam = lambda x: x % 2 == 0

print(is_even_lam(10))
print(is_even_lam(11))