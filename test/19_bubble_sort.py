numbers = [7, 3, 2, 1, 8]

# 0, 1, 2
for j in range(len(numbers)-1):
    for i in range(j + 1, len(numbers)):
    # ascending
        if numbers[j] > numbers[i]:
            numbers[j], numbers[i] = numbers[i], numbers[j]
print(numbers)

# Merge sort quick sort
