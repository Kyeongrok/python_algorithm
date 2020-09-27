def solution(numbers):
    s_l = list(map(str, numbers))
    s_l.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(s_l)))

print(solution([6, 10, 2]) == '6210')
print(solution([3, 30, 34, 5, 9]) == '9534330')
# print(solution([6, 10, 2, 70]) == '706210')
# print(solution([6, 10, 2, 70, 72]) == '72706210')
# print(solution([6, 10, 2, 70, 72, 998, 997, 1000]) == '72706210')

