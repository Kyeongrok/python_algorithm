numbers = [7, 3, 2, 9, 4] # => 2, 3, 4, 7, 9

def bubbleSort(arr):
    for front_index in range(0, len(arr) - 1):
        for index in range(front_index + 1, len(arr)):
            if arr[front_index] > arr[index]:
                temp = arr[front_index]
                arr[front_index] = arr[index]
                arr[index] = temp
    return arr

result = bubbleSort(numbers)
print(result)

