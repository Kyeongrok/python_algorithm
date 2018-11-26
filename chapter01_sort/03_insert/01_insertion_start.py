arr = [7, 3, 2, 9, 4]

def insertionSort(arr):
    for outterIndex in range(1, len(arr)):
        nowIndex = outterIndex
        while(nowIndex > 0 and arr[nowIndex - 1] > arr[nowIndex]):
            temp = arr[nowIndex-1]
            arr[nowIndex - 1] = arr[nowIndex]
            arr[nowIndex] = temp
            nowIndex = nowIndex - 1
            print(nowIndex, arr)
    return arr

print(insertionSort(arr))


