numbers = [7, 4, 5, 2]
# 0 1
# 1 2
# 2 3
# 0 1
# 1 2
# 2 3

# 0 1, 1, 2  until n-1 n
def insertion_sort(numbers):
    for _ in range(len(numbers) - 1):
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
    return numbers

print(insertion_sort(numbers))


