
def for_loop(n):
    if n > 0:
    # n번 만큼 for문을 반복 합니다
        for i in range(n):
            for_loop(n-1)
    else:
        return 0


for_loop(4)