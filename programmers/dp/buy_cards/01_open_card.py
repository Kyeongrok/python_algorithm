# i개
# N - i개

# D[N]이 N개를 구입하는 최대값
# D[N-1]은 N-1개를 구입하는 최대값
# P[i]는 i번째 카드팩이다.
# P[1] + ... + P[i] 면


# D[1], D[2] ... D[N-1], D[N] 이로케 구할 수 있습니다.
# 1개를 구입하는 최대값, 2개를 구입하는 최대값, N-1개를 구입하는 최대값, N개를 구입하는 최대값

def solution(N,P):
    D = [0] * N


    for i in range(1, N):
        D[0] = max(P[0], D[i - 1] + P[i ] )


print(solution(4, [1,5,6,7]))