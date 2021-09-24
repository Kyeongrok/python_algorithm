arr = [1, 2, 3, 4, 5, 6, 7]
def pick2(arr):
    list = []
    for index in range(2, len(arr)): # 1<= i < 7
        list.append((arr[1], arr[index]))
    return list
result = pick2(arr)
print(len(result))
print(result)
