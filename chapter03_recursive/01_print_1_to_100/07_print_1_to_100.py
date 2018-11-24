def print1To100(num):
    if num <= 100:
        print(num)
        print1To100(num + 1)

print1To100(1)