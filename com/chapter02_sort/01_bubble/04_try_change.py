numbers = [7, 3, 2, 9]  # => [2, 3, 7, 9]

first = numbers[0]
second = numbers[1]

temp = first
first = second
second = temp

print(first, second)