numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarySearch(arr, targetNum):
    midIndex = len(numbers) // 2
    if arr[midIndex] == targetNum:
        return midIndex

    return -1

print(binarySearch(numbers, 8))
