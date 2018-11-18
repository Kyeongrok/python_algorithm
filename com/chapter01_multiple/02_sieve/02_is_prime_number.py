def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True

for i in range(1, 100):
    print("{} {}".format(i, is_prime_number(i)))
