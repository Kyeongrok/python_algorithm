# 소수(prime)인지 판별하기 1

# 주어진 숫자까지 2부터 모두 나누어 보는 방법
def is_prime(num):
    for i in range(2, num//2 + 1):         # num // 2까지 반복
        if num % i == 0: return False # 나머지가 0인지
    return True

# 이유는 약수중에 가장 큰 것은 num // 2보다 작기 때문
# ex) 20의 약수는 20, 10, 5, 4, 2, 1 인데 이중 자신을 제외하고 가장 큰 것은 10
# ex2) 6 -> 6, 3, 2, 1

primes = []
for i in range(2, 100):
    if is_prime(i) == True:
        primes.append(i)
    print("{} {}".format(i, is_prime(i)))

print(primes)
