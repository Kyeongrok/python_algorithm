def search(arr, num):
    start = 0
    end = len(arr) - 1

    while(True):
        pivot = (start + end) // 2
        if arr[pivot] == num:
            return pivot
        elif arr[pivot] > num:
            end = pivot
        else:
            start = pivot

numbers = [1, 2, 3, 4, 5]
result = search(numbers, 4)
print(result)
