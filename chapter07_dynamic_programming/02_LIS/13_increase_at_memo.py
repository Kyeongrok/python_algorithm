numbers = [12, 49, 20, 4, 25, 2, 14]
memo = [1] * len(numbers)
print(len(numbers), len(memo))

for i in range(0, len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[i]:
            memo[i] = memo[i] + 1

