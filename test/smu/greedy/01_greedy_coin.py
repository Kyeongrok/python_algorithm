
# what is the problem?
# make amount using fewest coins

# 11 = 1 + 1 + 1 + 1 .... + 1

# 11 - 10 = 1
# try 1 - 10 but cannot
# try 11 - 5 = 6
# 11 - 5 = 6
# 6 - 5 = 1
# 6 - 2 = 4
# 4 - 2 = 2
# 2 - 2 = 0
# 5, 2, 2, 2 = 11
# 4

# amount - number until it can't

coins = [1, 2, 5, 10]
amount = 11
coins = sorted(coins, reverse=True)
count = 0
ans = []
for num in coins:
    while amount - num >= 0:
        amount -= num
        ans.append(num)
        count += 1

print(count, ans)

