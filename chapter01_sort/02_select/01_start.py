arr = [7, 3, 2, 9, 4]

def selectSort(arr, result):
    minValue = arr[0]
    minValueIndex = 0
    for i in range(0, len(arr)):
        print("----------")
        
        if arr[i] < minValue:
           minValue = arr[i]
           minValueIndex = i
    result.append(arr.pop(minValueIndex))
    if len(arr) == 0:
        return result
    else:
        return selectSort(arr, result)

print(selectSort(arr, []))

