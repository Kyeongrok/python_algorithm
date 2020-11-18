import matplotlib.pyplot as plt
def sum_of_digit(num):
    sum = 0
    while(num > 0):
        remainder = num % 10
        num = num // 10
        sum = sum + remainder
    return sum

def check_safe(size, limit):
    dp = [None] * size * 2
    memo = [[0] * size * 2 for _ in range(size * 2)]

    for i in range(-size, size):
        for j in range(-size, size):
            if dp[abs(i)] == None:
                dp[abs(i)] = sum_of_digit(abs(i))
            if dp[abs(j)] == None:
                dp[abs(j)] = sum_of_digit(abs(j))

            if dp[abs(i)] + dp[abs(j)] <= limit:
                memo[i+size][j+size] = 1
    return memo


size = 800
memo = check_safe(size, 23)

memo[size][size] = 2
safe_cnt = 1
tos = [
    [len(memo) - 1, len(memo) - 1, 1, 1], # increase x increase y
    [1, 1, -1, -1], # increase x decrease y
    [1, len(memo) - 1, -1, 1], # decrease x increase y
    [len(memo) - 1, 1, 1, -1] # increase x decrease y
]
for to in tos:
    for x in range(size, to[0], to[2]):
        for y in range(size, to[1], to[3]):
            if memo[y][x] == 2:
                continue
            elif memo[y][x] == 1 and 2 in [memo[y-1][x], memo[y+1][x], memo[y][x-1], memo[y][x+1]]:
                safe_cnt += 1
                memo[y][x] = 2
            else:
                memo[y][x] = 0

print('answer:', safe_cnt)
plt.imshow(memo)
plt.gca().invert_yaxis()
plt.show()