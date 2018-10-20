numbers = [7, 3, 2, 9]

for indexBack in range(1, len(numbers)):
    if numbers[0] > numbers[indexBack]:
        temp = numbers[0]
        numbers[0] = numbers[indexBack]
        numbers[indexBack] = temp

    print(numbers)