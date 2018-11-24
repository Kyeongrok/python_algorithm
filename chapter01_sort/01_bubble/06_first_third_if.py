numbers = [7, 3, 2, 9]
numbers = [3, 7, 2, 9]

first = numbers[0]
third= numbers[2]

if first > third:
    temp = first
    first = third
    third = temp

print(first, third)