numbers = [2, 7, 3, 9]

if numbers[0] > numbers[3]:
    temp = numbers[0]
    numbers[0] = numbers[3]
    numbers[3] = temp

print(numbers)