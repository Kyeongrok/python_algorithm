list = [9, 22, 3, 7, 4, 5]

def solution(list):
    for j in range(len(list)):
        for i in range(len(list)-j-1):
            print(i, j)
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        print(list)
    return list

def solution2(list):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            print(i, j)
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


print(solution(list))
# print(solution2(list))