def pic2(arr):
    list = []
    for index in range(1, len(arr)):
        tuple = (arr[0], arr[index])
        list.append(tuple)

    return list

arr = [1, 2, 3, 4, 5, 6, 7]
result = pic2(arr)
print(result)
print(len(result))
