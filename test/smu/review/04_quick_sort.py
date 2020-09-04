arr = [8, 2, 3, 9 ,4, 1]

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        smaller = []
        bigger = []

        for i in range(1, len(list)):
            if list[i] < pivot:
                smaller.append(list[i])
            else:
                bigger.append(list[i])
        return quick_sort(smaller) + [pivot] + quick_sort(bigger)

print(quick_sort(arr))