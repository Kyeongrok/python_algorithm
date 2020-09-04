def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = []
    greater = []

    for num in arr[1:]:
        if num < pivot:
            less.append(num)
        else:
            greater.append(num)

    return quick_sort(less) + [pivot] + quick_sort(greater)


def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(quick_sort(array[command[0] - 1:command[1]])[command[2] - 1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))