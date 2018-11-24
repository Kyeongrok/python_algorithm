arr = [7, 3, 2, 9, 4]

def select(arr, idx):
    if idx < len(arr):
        if arr[0] > arr[idx]:
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        return select(arr, idx + 1)
    else:
        return arr

print(select(arr, 1))
# 미완성임