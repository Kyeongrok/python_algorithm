arr = list(range(2, 100000000))
def binSearch(arr, num):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        midIndex = (start + end) // 2
        print("mi", midIndex, "mv:",arr[midIndex])
        if arr[midIndex] == num:
            return midIndex
        elif arr[midIndex] < num:
            start = midIndex + 1
        elif arr[midIndex] > num:
            end = midIndex - 1
    return - 1
print(binSearch(arr, 1))