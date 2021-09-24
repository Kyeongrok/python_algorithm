# 통과한 code
def solution(n, lost, reserve):

    _reserve = []
    for r in reserve:
        if r not in lost:
            _reserve.append(r)

    _lost = []
    for l in lost:
        if l not in reserve:
            _lost.append(l)

    # print(_lost, _reserve)
    memo = [0] * n
    for l in _lost:
        memo[l-1] = 1

    for r in _reserve:
        if r > 1 and memo[r-2] == 1:
            memo[r-2] = 0
        elif r < n and memo[r] == 1:
            memo[r] = 0

    # print(memo)
    return n - sum(memo)
# print(solution(5, [2, 4], [1, 3, 5]) == 5)
# print(solution(5, [2, 4], [3]) == 4)
# print(solution(3, [3], [1]) == 2)
# print(solution(2, [2], [1]) == 2)
print(solution(5, [2, 4], [2, 4]) == 5)

