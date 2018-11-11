numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        midIndex = (start + end) // 2
        if arr[midIndex] > targetNum:
            end = midIndex
        elif arr[midIndex] < targetNum:
            start = midIndex
        elif arr[midIndex] == targetNum:
            return midIndex

print(binarySearch(numbers, 8))
