numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 미완성
def binarySearch(arr, targetNum):
    start = 0
    end = len(arr)
    while(start <= end):
        midIndex = (start + end) // 2
        if arr[midIndex] > targetNum:
            start = midIndex
        elif arr[midIndex] < targetNum:
            end = midIndex

    return midIndex

print(binarySearch(numbers, 8))
