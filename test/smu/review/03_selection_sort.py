list = [3, 7, 5, 9, 1]
def selection_sort(list):
    for i in range(len(list)):
        min = list[i]
        index = i
        for j in range(i + 1, len(list)):
            if min > list[j]:
                min = list[j]
                index = j
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

print(selection_sort(list))

# 1
# 2
# 3
# 4
# 5

# 2
# 3
# 4
# 5