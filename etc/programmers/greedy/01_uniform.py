def solution(n, lost, reserve):
    lent = []

    inter = list(set(lost) & set(reserve))
    for i in inter:
        lost.remove(i)
        reserve.remove(i)

    lost_cnt = len(lost)
    for i in range(len(lost)):
        r = 0
        while len(lent) < lost_cnt and r < len(reserve):
            # print(i, r)
            if (lost[i] + 1 == reserve[r] or lost[i] - 1 == reserve[r]) and reserve[r] not in lent:
                lent.append(reserve.pop(r))
                break
            else:
                r+=1

    result = n - lost_cnt + len(lent)
    # print(n, lost_cnt, len(lent), len(list_lecture(set(lost) & set(reserve))), lent, result, list_lecture(set(lost) & set(reserve)))
    return result

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve) == 5)
print(solution(5, [1, 4], [1, 3, 5]) == 5)
print(solution(5, [1, 2, 4], [1, 3, 5]) == 5)
print(solution(3, [3], [1]) == 2)
