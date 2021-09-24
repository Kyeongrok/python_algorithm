def solution(numbers):
    result = 0
    for num in numbers:
        if num > result:
            result = num
        print(num, result)
    return result

numbers = [-9, -22, -3, -7, -4, -5]
print(solution(numbers))