
def optimalStrategy(coins):
    n = len(coins)
    dp = [[None] * n for i in range(n)]

    for j in range(n):
        dp[j][j] = (coins[j], 0)

    for j in range(n - 1):
        first = max(coins[j], coins[j+1])
        second = min(coins[j], coins[j+1])

        dp[j][j+1] = (first, second)

    for i in range(2, n):
        for j in range(0, n - i):
            print("j:{} {} j+i:{} {}".format(j, coins[j], j+i, coins[j+i]))
            print("아래", "왼쪽", coins[j:j+i+1]) # (0, 1), (1, 2)
            print(coins[j], dp[j + 1][j + i][0], dp[j][j + i - 1][0])
            print(coins[j+i], dp[j + 1][j + i][1], dp[j][j + i - 1][1])
            print(dp[j + 1][j + i], dp[j][j + i - 1])
            x = coins[j] + min(dp[j + 1][j + i][0], dp[j][j + i - 1][0])
            y = coins[j + i] + min(dp[j + 1][j + i][1], dp[j][j + i - 1][1])
            z = max(dp[j+1][j+i][1], dp[j][j+i-1][0])
            dp[j][j + i] = (max(x, y), z)
            print("--x:{}--y:{}--", x, y)

    for ddd in dp:
        print(ddd)

    return 0

coins = [2, 7, 40, 19]

result = optimalStrategy(coins)
