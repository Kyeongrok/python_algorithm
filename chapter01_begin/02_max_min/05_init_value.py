def solution(numbers):
    result = numbers[0] # numbers의 첫번째 값을 할당하고 시작
    for num in numbers:
        if num > result:
            result = num
        print(num, result)
    return result

numbers = [-9, -22, -3, -7, -4, -5]
print(solution(numbers))