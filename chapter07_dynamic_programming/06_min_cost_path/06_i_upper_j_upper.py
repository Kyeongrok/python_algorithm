def getMinCost(matrix):
    n = len(matrix)
    dp = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
            elif i > 0 and j > 0:
                dp[i][j] = min(
                    dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]) + matrix[i][j]

    for row in dp:
        print(row)

    return dp[n-1][n-1]

matrix = [
    [1,3,2],
    [4,6,2],
    [1,2,4]
]
print(getMinCost(matrix))
