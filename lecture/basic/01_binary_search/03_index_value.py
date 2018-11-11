numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1
    midIndex = (start + end) // 2
    indexValue = arr[midIndex]
    print(start, end, midIndex, "indexValue:",indexValue)

    if indexValue == targetNum:
        return midIndex
    return -1

print(binarySearch(numbers, 4))
