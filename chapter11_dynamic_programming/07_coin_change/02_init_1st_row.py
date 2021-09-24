coins= [1, 3, 4, 5]
amount = 7
memo = [[0] * (amount + 1) for _ in range(len(coins))]

for j in range(amount + 1):
    memo[0][j] = j

for i in range(amount + 1):
    if i < coins[1]:
        memo[1][i] = memo[1-1][i]

print(memo)



