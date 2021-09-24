numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarySearch(arr, start, end, targetNum):
    midIndex = (start + end) // 2
    if arr[midIndex] == targetNum:
        return midIndex
    elif arr[midIndex] > targetNum:
        return binarySearch(arr, start, midIndex - 1, targetNum)
    elif arr[midIndex] < targetNum:
        return binarySearch(arr, midIndex + 1, end, targetNum)

    return -1

print(binarySearch(numbers, 0, len(numbers)-1, 8))
