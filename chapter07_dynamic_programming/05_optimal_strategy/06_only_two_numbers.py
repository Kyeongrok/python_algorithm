def optimalStrategy(coins):
    n = len(coins)
    dp = [[0] * n for i in range(n)]

    # 숫자가 1개만 있는 경우
    for j in range(0, n):
        dp[j][j] = (coins[j], 0)

    # 숫자가 2개만 있는 경우
    for j in range(0, n - 1):
        first = max(coins[j], coins[j+1])
        second = min(coins[j], coins[j+1])
        dp[j][j+1] = (first, second)

    print(dp)
    return 0

coins = [2, 7, 40, 19]
result = optimalStrategy(coins)

print(result)