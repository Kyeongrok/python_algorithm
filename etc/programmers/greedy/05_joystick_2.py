def shortest_next(name):
    min_move = len(name) - 1
    for i in range(len(name)):
        # a가 아닌 알파벳이 나오는 idx까지 역으로 가는 경우
        if name[i] != 'A':
            next = i + 1
            while next < len(name) and name[next] == 'A':
                next += 1
            move = 2 * i + len(name) - next
            min_move = min(move, min_move)
    return min_move


def shortest_y(c):
    # 1234567890123 4567890123456
    # ABCDEFGHIJKLM NOPQRSTUVWXYZ

    # A에서 B가려면 1번 움직이면 되고 A에서 M가려면 12번 움직이거나 한번 움직인다.
    # A가 가장 작기 때문에 -가 나올 일은 없고 0은 나올 수 있다. A -> A

    # 반대의 경우 A에서 Y까지 가려면 24번 움직여야 한다.
    # 하지만 2번만에 갈 수도 있다.
    return min(ord(c) - 65, 26 - (ord(c) - 65))


def solution(name):
    cnt = 0
    # 알파벳 최소
    for c in name:
        cnt += shortest_y(c)

    # 좌우 이동 최소
    cnt += shortest_next(name)
    return cnt


# print(solution() == 0)
# print(shortest_y('B') == 1)
# print(shortest_y('Z') == 1)
# print(shortest_y('M') == 12)
# solution('JAZ')
print(shortest_next('ABABAAAAB'))
print(solution('ABABAAAAB'))

