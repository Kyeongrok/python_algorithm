arr = [7, 2, 3, 9, 28, 11]

if arr[0] > arr[1]:
    temp = arr[0]
    arr[0] = arr[1]
    arr[1] = temp

print(arr)

for j in range(len(arr) - 1):
    for i in range(j + 1, len(arr)):
        if arr[j] > arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        print(f'j:{j} i:{i} arr:{arr}')

