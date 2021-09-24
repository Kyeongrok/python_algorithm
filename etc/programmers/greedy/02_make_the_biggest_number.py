from random import randint
import numpy as np

def solution(number, k):
    answer = ''

    remain = number

    while k > 0 and len(remain) > 1:
    # for _ in range(4):
        mid = len(remain) // 2
        left = remain[:mid]
        right = remain[mid:]
        left_max = int(left[0])
        max_idx = 0
        for i in range(1, len(left)):
            if int(left_max) < int(left[i]):
                left_max, max_idx = int(left[i]), i
        answer += str(left_max)
        k -= max_idx
        remain = left[max_idx+1:] + right
        print(answer, remain, max_idx, k)
    return str(answer) + str(remain)


# print(solution("1924", 2) == "94")
# print(solution("1111111119",9) == '9')
# print(solution("1231234",3) == '3234')
# print(solution('4177252841',4) == '775841')
# print(solution('417792252289841',4) == '92252289841')
