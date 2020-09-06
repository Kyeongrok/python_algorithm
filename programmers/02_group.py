def solution(scores, k):
    answer = 5
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
            elif j + 1 > i:
                ll = []
                for l in range(1, j - 1):
                    print(j, l, dp[i - l][j - 1], dp[i - 1][j - l] , scores[j], scores[j-l])
                    min_val = min(dp[i - 1][j - 1], dp[i - 1][j - l] + scores[j] - scores[j - l])
                    ll.append(min_val)
                # dp[i][j] = min(ll)
    print(dp)
    # n과 n+1의
    return answer


print(solution([1,2,12,14,15], 2) == 4)