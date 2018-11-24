def findSmallestIndex(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    resultArr = []
    for i in range(len(arr)):
        smallest = findSmallestIndex(arr)   # 가장 작은 숫자의 인덱스를 찾는다.
        resultArr.append(arr.pop(smallest))    # 해당 인덱스에서 뽑아다가 resultArr에 넣는다.
    return resultArr

print(selectionSort([5, 3, 6, 2, 10]))
