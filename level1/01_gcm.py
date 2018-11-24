def gcm(first, second):
    if first == second:
        return first
    elif first > second:
        return gcm(first - second, second)
    else:
        return gcm(first, second - first)

print(gcm(196, 42))
