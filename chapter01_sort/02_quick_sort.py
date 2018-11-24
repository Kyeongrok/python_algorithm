import numpy as np

numbers = np.random.randint(1, 50, size=10)
print(numbers)
print(numbers[1:])

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

result = quick_sort(numbers)
print(result)


