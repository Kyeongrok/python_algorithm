numbers = [2, 7, 3, 9]

for ib in range(2, len(numbers)):
   if numbers[1] > numbers[ib]:
       temp = numbers[1]
       numbers[1] = numbers[ib]
       numbers[ib] = temp

   print(numbers)