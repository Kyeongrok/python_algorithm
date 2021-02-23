# 소수(prime)인지 판별하기 1

# 주어진 숫자까지 2부터 모두 나누어 보는 방법
def is_prime(num):
    for i in range(2, num):         # 2부터 반복
        if num % i == 0: return False # 나머지가 0인지
    return True

primes = []
for i in range(2, 100): # 1은 소수의 정의는 만족하지만 소수가 아니다
    if is_prime(i) == True:
        primes.append(i)
    print("{} {}".format(i, is_prime(i)))

print(primes)
