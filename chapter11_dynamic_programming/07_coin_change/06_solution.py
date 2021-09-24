# coin changing
coins = [1, 3, 4, 5]
aim = 7

memo = [[0] * (aim + 1) for _ in range(len(coins)) ]

for i in range(len(coins)):
    for j in range(aim + 1):
        if j == 0:
            memo[i][j] = 0
        if i == 0:
            memo[i][j] = j

        if i != 0 and coins[i] < j: # i = 1 => 3
            above = memo[i-1][j]
            memo[i][j] = min(above, memo[i][j-coins[i]] + 1)
        elif coins[i] > j:
            memo[i][j] = memo[i-1][j]
        elif coins[i] == j:
            memo[i][j] = 1



for row in memo:
    print(row)