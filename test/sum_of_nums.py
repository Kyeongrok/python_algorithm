def solution(a, b):
    return sum(range(a, b))

print(solution(3, 5)) # 7
print(solution(3, 6)) # 12

# 3 + 4 + 5 = 12
# 3 + 4 + 5 + 6 = 18

# 3, 6 넣으면 18이 나와야 하는데 12가 나옴
# 3, 5 넣으면 12가 나와야 하는데 7이 나옴
range(1, 3)