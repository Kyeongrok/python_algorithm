numbers = [7, 3, 2, 9]
    # [3, 7, 2, 9]
    # [2, 7, 3, 9]
numbers = [2, 7, 3, 9]
    # [2, 3, 7, 9] n n+1
    # [2, 3, 7, 9] n n+1
numbers = [2, 3, 7, 9]


# 0번째와 나머지를 모두 비교를 한다. 1바퀴
# 가장 작은게 0번째에 온다.
# 그 다음으로 작은게 1번째에 오게 해야 한다.

for index in range(1, len(numbers)): # 1, 2, 3
    if numbers[2] > numbers[index]: # 7 > 3 = true
        # 자리를 바꿔준다.
        temp = numbers[2]
        numbers[2] = numbers[index]
        numbers[index] = temp
    print(numbers)

# n = 1
# 1 2   n, n+1
# 1 3   n, n+2

# 0 1 2