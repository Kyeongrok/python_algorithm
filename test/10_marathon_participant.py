def solution(participant, completion):
    participant.sort()
    completion.sort()




aa = (['aaa', 'bbb', 'bbb'], ['aaa', 'bbb'])
bb = (['aaa', 'bbb', 'ccc'], ['aaa', 'bbb'])


print(solution(aa[0], aa[1]) == 'bbb')
print(solution(bb[0], bb[1]) == 'ccc')
# 4:20