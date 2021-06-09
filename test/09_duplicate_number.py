def duplicate_number(arr):
    seen = set()

    for i in range(len(arr)):
        if i in seen:
            return arr[i]
        else:
            seen.add(arr[i])
    return -1


# -1, 1은 같은 것으로
def duplicate_number_advanced(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i]) - 1] < 0:
            return abs(arr[i])
        else:
            pass


arr = [2, 1, 3, 5, 3, 2]


print(duplicate_number(arr))
