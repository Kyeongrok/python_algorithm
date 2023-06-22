arr = [7, 2, 3, 9, 28, 1]


for j in range(len(arr) - 1):
    for i in range(len(arr) - 1 - j):
        if arr[i] < arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
        print(f'j:{j} i:{i} {arr}')
print(arr)




