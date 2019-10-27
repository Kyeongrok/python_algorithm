def getMaxColumnSum(matrix):
    n = len(matrix)
    memo = [0] * n

    for j in range(n):
        columnSum = 0
        for i in range(n):
            columnSum += matrix[i][j]
        memo[j] = columnSum

    return max(memo)

matrix = [
    [0, 0.5, 0.5, 0.6],
    [0.5, 0, 0, 0.3],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

result = getMaxColumnSum(matrix)
print(result)
