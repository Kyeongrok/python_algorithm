arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1
    midIndex = len(arr) // 2
    indexValue = arr[midIndex]
    if indexValue == targetNum:
        return midIndex
    elif indexValue < targetNum:
        start = midIndex + 1
    elif indexValue > targetNum:
        end = midIndex - 1

    print("start:",start, "end:", end)
    return -1

# 1------5----8--11
# 5----8--11
print(binarySearch(arr, 8))