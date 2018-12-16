arr = [1, 2, 3, 4, 5, 6, 7]
def pick2(arr):
    list = []
    list.append((arr[0], arr[1]))
    list.append((arr[0], arr[2]))
    list.append((arr[0], arr[3]))
    return list

print(pick2(arr))