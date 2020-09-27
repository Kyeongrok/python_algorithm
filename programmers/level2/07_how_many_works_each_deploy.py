import math
def solution(progresses, speeds):
    answer = []

    d = 0
    l = 0
    for i in range(len(progresses)):
        r_time = math.ceil((100 - progresses[i]) / speeds[i])
        if l == 0:
            d = 1
            l = r_time
        elif l - r_time >= 0:
            d += 1
            l = r_time
        else:
            # print(r_time)
            answer.append(d)
            d = 1
            l = r_time
    answer.append(d)
    print(answer)

    return answer


print(solution([93, 30, 55], [1, 30, 5]) == [2, 1])
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]) == [1, 3, 2])
print(solution([5, 15, 15, 99],[1, 1, 1, 1]) == [4])
print(solution([99, 15, 15, 98, 44],[1, 2, 2, 1, 30]) == [1,4])
# print(solution([99, 15, 15, 98, 44],[99, 2, 2, 1, 30]) == [1,3])
# print(solution([99, 15, 15, 98],[1, 2, 1, 1]) == [1,3])

'''
test case는 2개 통과
전체 통과했는지는 아직 모름
'''