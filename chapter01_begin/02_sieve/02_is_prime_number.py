def isPrimeNumber(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True

primes = []
for i in range(1, 100):
    if isPrimeNumber(i) == True:
        primes.append(i)
    print("{} {}".format(i, isPrimeNumber(i)))

print(primes)
