def solution(w,h):

    sum1 = 0
    for i in range(w):
        y = w / h * i
        print(i, y)
        # print(i, y, y.is_integer())
        if y >= 1:
            if y.is_integer():
                sum1 += (int(y) - 1)
            else:
                sum1 += int(y)


    print(sum1)
    return w * h - sum1


print(solution(8, 12) == 80) # w, h
# print(solution(1, 12) == 0)
# print(solution(2, 4) == 2)
