def solution(numbers):
    result_idx = 0 # 여기에서 0은 0번 인덱스
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[result_idx]:
            result_idx = i
        print(i, numbers[i], result_idx)
    return result_idx

numbers = [-9, -22, -3, -7, -4, -5]
print(solution(numbers))
