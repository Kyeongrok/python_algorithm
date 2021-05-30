def solution(numbers):
    result = 0
    for num in numbers:
        if num > result: # num과 지금까지의 가장 큰수 비교
            result = num # 조건에 맞으면 교체
        print(num, result)
    return result

numbers = [9, 22, 3, 7, 4, 5]
print(solution(numbers))