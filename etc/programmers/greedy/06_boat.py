def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)

    po_f = 0
    po_b = len(people) - 1

    while po_f <= po_b:
        # print(limit, people[po_f], people[po_b], po_f, po_b, limit - people[po_f] - people[po_b])
        if len(people) == 1:
            answer += 1
        elif limit - people[po_f] == 0:
            po_f += 1
            answer += 1
        elif len(people) > 1 and limit - people[po_f] - people[po_b] >= 0:
            answer += 1
            po_f += 1
            po_b -= 1
        elif limit - people[po_f] > 0 and limit - people[po_f] - people[po_b] < 0:
            answer += 1
            po_f += 1
            # print('---c4---')
        else:
            print('wrong limit')

    # print(answer)
    return answer


print(solution([70, 50, 80, 50], 100) == 3)
print(solution([70, 80, 50], 100) == 3)
print(solution([130, 80, 110], 240) == 2)
print(solution([40,40,40,40,40,40,], 40) == 6)
