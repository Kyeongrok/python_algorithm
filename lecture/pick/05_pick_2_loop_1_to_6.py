arr = [1, 2, 3, 4, 5, 6, 7]
def pickN(arr):
    list = []
    for indexLv1 in range(0, len(arr)):
        for indexLv2 in range(indexLv1 + 1, len(arr)): # 1<= i < 7
            list.append((arr[indexLv1], arr[indexLv2]))
    return list
result = pickN(arr)
print(len(result))
print(result)
