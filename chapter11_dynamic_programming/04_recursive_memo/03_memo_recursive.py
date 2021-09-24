# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 10
memo = [0] * n
print(memo, len(memo))

def checkMemo(memo, n):
    print(n, memo)
    if n <= 0:
        print("return:", memo)
        return memo
    else:
        n = n - 1
        memo[n] = n
        checkMemo(memo, n)

result = checkMemo(memo, n)
print("result:", result)