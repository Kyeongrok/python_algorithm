numbers = [2, 7, 3, 9]

for indexFront in range(0, 1+1):
    for indexBack in range(2, len(numbers)):
       if numbers[1] > numbers[indexBack]:
           temp = numbers[1]
           numbers[1] = numbers[indexBack]
           numbers[indexBack] = temp

       print(numbers)