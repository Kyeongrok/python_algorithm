def solution(list):
    result = 0
    for num in list:
        if num > result:
            result = num
        print(num, result)
    return result

list = [-9, -22, -3, -7, -4, -5]
print(solution(list))