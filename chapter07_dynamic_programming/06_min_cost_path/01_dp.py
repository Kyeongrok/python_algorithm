def getMinCost(matrix):
    n = len(matrix)
    dp = [[0] * n for i in range(n)]

    for row in dp:
        print(row)

    return 0

matrix = [
    [1,3,2],
    [4,6,2],
    [1,2,4]
]
print(getMinCost(matrix))