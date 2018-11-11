numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1
    midIndex = (start + end) // 2
    print(start, end, midIndex)
    return -1
print(binarySearch(numbers, 8))
