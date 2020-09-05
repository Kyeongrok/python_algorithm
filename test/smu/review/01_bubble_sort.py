# [7, 4, 5, 2]
# 4 7 5 2   # 7 4   0 1
# 4 5 7 2   # 7 5   1 2
# 4 5 2 7   # 7 2   2 3


numbers = [1, 7, 8, 3, 17, 13] #()

# index and value

# 0 1 ---> 1 7
# 0 2 ---> 1 8
# 0 3 ---> 1 3
# 0 4
# 0 5
# ------------ 1 round ---------
# 1 2
# 1 3
# 1 4
# 1 5
# ----------- 2nd round ---------
# 2 3



def bubble_sort(numbers):
    for j in range(len(numbers) - 1):
        for i in range(j + 1, len(numbers)):
            print(j, i)
            if numbers[j] > numbers[i]:
                temp = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = temp
    return numbers

print(bubble_sort(numbers))
