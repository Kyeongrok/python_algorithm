numbers = [5, 3, 6, 2, 10]

def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):    # 앞에는 이미 정렬 되어 있어서 i보다 1개 큼
            if(arr[j] < arr[i]):
                temp = arr[i]   # i값이 없어지지 않게 임시보관함
                arr[i] = arr[j]
                arr[j] = temp
        print("i:", i, "arr:", arr) # 중간 과정

    return arr

result = bubbleSort(numbers)
print(result)