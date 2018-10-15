import numpy as np

numbers = np.random.randint(1, 10000, size=10000)

print(numbers)
print(numbers[1:])

def quickSort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quickSort(less) + [pivot] + quickSort(greater)

result = quickSort(numbers)
print(result)
