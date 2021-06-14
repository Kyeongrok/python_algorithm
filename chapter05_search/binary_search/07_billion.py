arr = list(range(1, 100000000))

def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        midIndex = (start + end) // 2
        print(midIndex)
        if arr[midIndex] == targetNum:
            return midIndex
        elif arr[midIndex] < targetNum:
            start = midIndex + 1
        elif arr[midIndex] > targetNum:
            end = midIndex - 1
    return -1
print(binarySearch(arr, 9610))