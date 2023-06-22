arr = [7, 2, 3, 9, 28, 11]

if arr[0] > arr[1]:
    # swap
    temp = arr[0]
    arr[0] = arr[1]
    arr[1] = temp

print(arr)

if arr[1] > arr[2]:
    temp = arr[1]
    arr[1] = arr[2]
    arr[2] = temp

print(arr)

if arr[2] > arr[3]:
    temp = arr[2]
    arr[2] = arr[3]
    arr[3] = temp

print(arr)

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        # swap
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
