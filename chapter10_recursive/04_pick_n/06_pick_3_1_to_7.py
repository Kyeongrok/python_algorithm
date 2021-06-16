arr = [1, 2, 3, 4, 5, 6, 7]
def picN(arr):
    list = []
    for indexLv1 in range(0, len(arr)):
        pickArr = []
        pickArr.append(arr[indexLv1])
        for indexLv2 in range(indexLv1 + 1, len(arr)):
            pickArr.append(arr[indexLv2])
            for indexLv3 in range(indexLv2 + 1, len(arr)):
                arr[indexLv3]
                list.append(pickArr)
    return list
result = picN(arr)
print(len(result))
print(result)
