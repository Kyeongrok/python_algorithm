numbers = [7, 3, 2, 9]

for ib in range(1, len(numbers)):
    if numbers[0] > numbers[ib]:
        temp = numbers[0]
        numbers[0] = numbers[ib]
        numbers[ib] = temp

    print(numbers)