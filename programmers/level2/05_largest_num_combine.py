def sep_num(n):
    l = []
    sep = pow(10,(len(str(n)) - 1))
    while sep >= 1:
        q = n // sep
        r = n % sep
        l.append(int(q))
        n = r
        sep /= 10
    return l

def l1(l1, l2):
    if l1[0] > l2[0]:
        return 1
    else:
        return 0

def solution(numbers):
    answer = ''

    sorted_numbers = []
    for n in numbers:
        sorted_numbers.append(sep_num(n))
    sorted_numbers = sorted(sorted_numbers, reverse=True)

    for i in range(1, len(sorted_numbers)):
        a = sorted_numbers[i-1]
        b = sorted_numbers[i]
        if a[0] == b[0] and len(a) > len(b) and a[1] < b[0]:
            tmp = sorted_numbers[i-1]
            sorted_numbers[i-1] = b
            sorted_numbers[i] = tmp

    # print(sorted_numbers)

    for n in sorted_numbers:
        for c in n:
            answer += str(c)
    return answer


print(solution([6, 10, 2]) == '6210')
print(solution([3, 30, 34, 5, 9]) == '9534330')
# print(solution([6, 10, 2, 70]) == '706210')
# print(solution([6, 10, 2, 70, 72]) == '72706210')
# print(solution([6, 10, 2, 70, 72, 998, 997, 1000]) == '72706210')
