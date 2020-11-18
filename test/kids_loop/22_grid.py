import matplotlib.pyplot as plt
def sum_of_digit(num):
    sum = 0
    while(num > 0):
        remainder = num % 10
        num = num // 10
        sum = sum + remainder
    return sum

memo = [[0] * 2000 for _ in range(2000)]
dp = [None] * 2000

area = 0
for i in range(-1000, 1000):
    for j in range(-1000, 1000):
        if dp[abs(i)] == None:
           dp[abs(i)] = sum_of_digit(abs(i))
        if dp[abs(j)] == None:
            dp[abs(j)] = sum_of_digit(abs(j))

        if dp[abs(i)] + dp[abs(j)] <= 23:
            memo[i+1000][j+1000] = 1

for i in range(-1000, 1000):
    for j in range(-1000, 1000):
        pass

print(area)
plt.imshow(memo)
plt.gca().invert_yaxis()
plt.show()
