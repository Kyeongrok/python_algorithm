# 재귀로 풀기
import math

def sieve_multiple_n(arr, diviser, last):
    result = []
    for number in arr:
        if number == diviser or number % diviser != 0:
            result.append(number)
    if diviser == last:
        return result
    else:
        return sieve_multiple_n(result, diviser + 1, last)

arr = list(range(2, 54))# 1은 소수가 아니기 때문에 제외
res = sieve_multiple_n(arr, 2,int(math.sqrt(len(arr))))
print(res)
