from math import sqrt

N = 50
ns = list(range(2, N + 1)) # 2부터 50까지 숫자 생성

for i in range(2, int(sqrt(N)) + 1): # 루트 N이하의 자연수
    print(i)
