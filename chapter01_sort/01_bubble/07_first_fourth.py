numbers = [7, 3, 2, 9]
numbers = [3, 7, 2, 9]
numbers = [2, 7, 3, 9]

first = numbers[0]
fourth= numbers[3]

if first > fourth:
    temp = first
    first = fourth
    fourth = temp

print(first, fourth)