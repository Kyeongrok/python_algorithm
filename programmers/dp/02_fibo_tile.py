# N = 5 -> 26
# N = 6 -> 42

def solution(N):

    if N == 1:
        return 4

    memo = [None] * N
    memo[0] = 1
    memo[1] = 1

    for i in range(2, N):
        memo[i] = memo[i - 1] + memo[i - 2]
    return 4 * memo[N - 1] + 2 * memo[N - 2]

print(solution(1))
print(solution(2))
print(solution(5))
