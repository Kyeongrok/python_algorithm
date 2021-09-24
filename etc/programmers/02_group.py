# max - min이 최소가 되는 점수를 return
# 팀을 k개로 쪼갤 때
def solution(scores, k):
    scores = sorted(scores)
    dp = [[None] * len(scores) for i in range(k)]
    '''
            1   3   7                                           
        1   0   2   6                                           
        2   x   0   min(dp[i-1][j-1], dp[i-2][j-1] + scores[i]-scores[i-1])
        3
    '''
    for i in range(k):
        for j in range(len(scores)):
            if i == j:
                dp[i][j] = 0
            elif i == 0 and j > 0:
                dp[i][j] = scores[j] - scores[0]
            elif j > i:
                ll = [dp[i - 1][j - 1]]

                for l in range(1, j):
                    # j가 2면 2개를 더하고 j가 3이면 3개를 더해야 한다.
                    min_val = dp[i - 1][j - l - 1] + scores[j] - scores[j - l]
                    ll.append(min_val)
                    # print(i, j, l, ll)
                    print(ll)
                dp[i][j] = min(ll)
    for d in dp:
        print(d)
    # n과 n+1의
    return dp[k-1][len(scores)-1]


# print(solution([1,2,12,14,15], 2) == 4)
# print(solution([1,2,12,14,15,16], 2) == 5)
print(solution([1,2,12,14,15,20], 2) == 9)
# print(solution([1,2,12,14,15], 3) == 2)
# print(solution([2,12,14,15], 3) == 1)
