# array에 중간 결과를 저장한다.
# 중간 결과는 parameter로 recursive 구간을 돌아다닌다.

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(3))