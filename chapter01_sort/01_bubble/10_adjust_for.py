numbers = [7, 3, 2, 9]

for indexBack in range(1, 3+1):
    if numbers[0] > numbers[3]:
        temp = numbers[0]
        numbers[0] = numbers[3]
        numbers[3] = temp

    print(numbers)