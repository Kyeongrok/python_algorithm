h = 9
pivot = h // 2
for i in range(h):
    if i <= pivot:
        print(f"{i}{' ' * (pivot - i)}{'*' * (2 * i + 1)}")
    else:
        print(f"{i}{' ' * (i - pivot)}{'*'*(2 * (h - i) - 1)}")