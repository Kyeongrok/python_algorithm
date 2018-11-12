arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

def binarySearch(arr, targetNum):
    midIndex = len(arr) // 2
    indexValue = arr[midIndex]
    if indexValue == targetNum:
        return midIndex

    print(midIndex, indexValue)
    return -1

print(binarySearch(arr, 8))