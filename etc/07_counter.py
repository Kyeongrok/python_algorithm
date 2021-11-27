from collections import Counter


numbers = [4, 0, 4, 4, 1, 8, 8, 2, 2, 5, 0, 6, 5, 6, 0]
numbers = sorted(numbers)
for k, v in Counter(numbers).items():
    print(k, v)