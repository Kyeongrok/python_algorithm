
pivot = None
list = [2, 9, 0 ,3 ,1 ,6, 8]
def quick_sort(list):
    print(list)
    if len(list) > 1:
        pivot = list[0]
        less = []  # 0 1
        greater = []  # 9 3 6 8
        for num in list[1:]:
            if pivot > num:
                less.append(num)
            elif num > pivot:
                greater.append(num)
        return quick_sort(less) + [pivot] + quick_sort(greater)
    else:
        return list


result = quick_sort(list)
print(result)