'''
문제 1.
1 ~ n 까지의 숫자 중 소수 (1 과 자기자신으로만 나누어지는 수) 를 출력하는 코드를 작성해보자.
'''

# 1, 2, 3, 5, 7, 11
import math

def solution(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sieve(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while(p * p <= n):
        if prime[p] == True:
            for i in range(p*2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            print(p)
sieve(10)

