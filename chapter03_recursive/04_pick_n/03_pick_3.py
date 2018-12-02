arr = [1, 2, 3, 4, 5, 6, 7]
def pic3(arr):
    list = []
    for index in range(3, len(arr)):
        tuple = (arr[2], arr[index])
        list.append(tuple)
    return list

print(pic3(arr))