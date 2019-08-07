def getMinCost(matrix):
    n = len(matrix)
    dp = [[0] * n for i in range(n)]

    # i는 행, j는 열
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = matrix[i][j]
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j-1] + matrix[i][j]

    for row in dp:
        print(row)

    return 0

matrix = [
    [1,3,2],
    [4,6,2],
    [1,2,4]
]
print(getMinCost(matrix))
