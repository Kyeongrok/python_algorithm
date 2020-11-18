import matplotlib.pyplot as plt
def sum_of_digit(num):
    sum = 0
    while(num > 0):
        remainder = num % 10
        num = num // 10
        sum = sum + remainder
    return sum

def max_sum(num):

    # 27 = 999
    # 23 = 994
    # 22 = 993
    # 9 9 = 18
    # 9 2 = 11
    # 9 1 = 10
    # 9 0 = 9
    # 0 8 = 8
    quotient = num // 9
    remainder = num % 9




def check_safe(limit):
    dp = [None] * 2000
    memo = [[0] * 2000 for _ in range(2000)]
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if dp[abs(i)] == None:
               dp[abs(i)] = sum_of_digit(abs(i))
            if dp[abs(j)] == None:
                dp[abs(j)] = sum_of_digit(abs(j))

            if dp[abs(i)] + dp[abs(j)] <= limit:
                memo[i+1000][j+1000] = 1
    return memo

def check_available(memo):
    memo[1000][1000] = 2

    is_changing = True
    cnt = 0
    while is_changing:
        cnt += 1
        is_changing = False
        for y_idx in range(1, len(memo) - 1):
            for x_idx in range(1, len(memo[y_idx]) - 1):
                if memo[y_idx][x_idx] == 2:
                    print('{}---safe---'.format(cnt))
                    continue
                elif memo[y_idx][x_idx] != 0 and 2 in [memo[y_idx-1][x_idx], memo[y_idx+1][x_idx], memo[y_idx][x_idx-1], memo[y_idx][x_idx+1]]:
                    memo[y_idx][x_idx] = 2
                    is_changing = True


memo = check_safe(23)
memo = check_available(memo)
plt.imshow(memo)
plt.gca().invert_yaxis()
plt.show()
