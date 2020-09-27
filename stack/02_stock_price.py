from collections import deque
def solution(prices):

    d = deque()
    memo = [0] * len(prices)

    for i in range(len(prices)):
        n = prices[i]
        while len(d) > 0 and n < prices[d[-1]]:
            top = d.pop()
            memo[top] = i - top
        d.append(i)

    # print(d, memo)
    while len(d) > 0:
        last = d.pop()
        memo[last] = len(prices) - 1 -last
    # print(memo)
    return memo

# print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
print(solution([3, 4, 2, 2, 3]) == [2, 1, 2, 1, 0])
# print(solution([1, 2, 2, 2, 3]) == [4, 3, 2, 1, 0])
# print(solution([1, 4, 3, 2, 2]) == [4, 1, 1, 1, 0])
# print(solution([4, 3, 3, 2, 2]) == [1, 2, 1, 1, 0])
