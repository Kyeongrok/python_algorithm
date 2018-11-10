numbers = [7, 3, 2, 9, 4]

for indexFront in range(0, len(numbers) - 1):
    for indexBack in range(indexFront + 1, len(numbers)):
       if numbers[indexFront] > numbers[indexBack]:
           temp = numbers[indexFront]
           numbers[indexFront] = numbers[indexBack]
           numbers[indexBack] = temp

       print(numbers)