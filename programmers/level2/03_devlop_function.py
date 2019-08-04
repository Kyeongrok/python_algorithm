import math

def solution(progresses, speeds):
    answer = []
    memo = [0] * len(progresses)

    latestNum = 0
    for i in range(len(progresses)):
        memo[i] = math.ceil((100 - progresses[i]) / speeds[i])
        if(len(answer) == 0):
            answer.append(1)
            latestNum = memo[i]
        elif(latestNum >= memo[i]):
            answer[len(answer)-1] += 1
        else:
            answer.append(1)
            latestNum = memo[i]
    return answer

print(solution([93,30,55],[1,30,5]))
print(solution([93,30,55,40],[1,30,5,2]))
print(solution([30],[90]))
print(solution([33,34],[1,1]))
print(solution([34,34],[1,1]))
# print(solution([35,34],[3,1]))
# print(solution([30,55,40,7],[30,5,2,90]))
# print(solution([30,55,40,7],[1,5,2,90]))
# print(solution([30,55,40,7],[90,1,2,3]))

