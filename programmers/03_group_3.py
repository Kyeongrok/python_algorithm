# 팀을 k개로 쪼갤 때 max - min이 최소가 되는 점수를 return
#
def solution(scores, k):
    scores = sorted(scores)
    dp = [[0] * len(scores) for i in range(k)]
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
                    min_val = dp[i - 1][j - l - 1] + scores[j] - scores[j - l]
                    ll.append(min_val)
                dp[i][j] = min(ll)
    for d in dp:
        print('dp:',d)
    return dp[k-1][len(scores)-1]

print(solution([1,2,12,14,15], 2) == 4)
print(solution([1,2,12,14,15,16], 2) == 5)
print(solution([1,2,12,14,15,20], 2) == 9)
print(solution([1,2,12,14,15], 2) == 4)
print(solution([1,2,12,14], 3) == 1)
print(solution([1,2,12,14,15], 3) == 2)
print(solution([2,12,14,15], 3) == 1)

'''
앞에 코드와 차이점은 
dp = [[None] * len(scores) for i in range(k)]
dp = [[0] * len(scores) for i in range(k)]
이거 차이였음. 
solution([1,2,12,14], 3)의 경우
1, 2, 12 만 있을때의 2개 solution([1,2,12], 2)에서 계산해 놓은 것을 참조한다.
그런데 None이면 0으로 계산 되어야 할 것이 None이므로 +연산이 안되서 에러가 난다.
'''