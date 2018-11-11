def search(arr, num):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        pivot = (start + end) // 2
        if arr[pivot] == num:
            return pivot
        elif arr[pivot] > num:
            end = pivot
        else:
            start = pivot

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = search(numbers, 4)
print(result)
