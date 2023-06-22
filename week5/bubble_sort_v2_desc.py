arr = [7, 2, 3, 9, 28, 11]

for j in range(len(arr) - 1):
    for i in range(j + 1, len(arr)):
        if arr[j] < arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        print(f'j:{j} i:{i} arr:{arr}')

