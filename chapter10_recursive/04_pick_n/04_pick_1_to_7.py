arr = [1, 2, 3, 4, 5, 6, 7]
def picN(arr):
    list = []
    for indexLv1 in range(0, len(arr)):
        for indexLv2 in range(indexLv1 + 1, len(arr)):
            tuple = (arr[indexLv1], arr[indexLv2])
            list.append(tuple)
    return list
result = picN(arr)
print(len(result))
print(result)
