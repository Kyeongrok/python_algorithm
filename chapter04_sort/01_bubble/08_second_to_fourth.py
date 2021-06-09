# first second
numbers = [7, 3, 2, 9]

first = numbers[0]
second = numbers[1]

temp = first
first = second
second = temp

#first third
numbers = [3, 7, 2, 9]

first = numbers[0]
third= numbers[2]

if first > third:
    temp = first
    first = third
    third = temp

# first fourth
numbers = [2, 7, 3, 9]

first = numbers[0]
fourth= numbers[3]

if first > fourth:
    temp = first
    first = fourth
    fourth = temp

print(first, fourth)