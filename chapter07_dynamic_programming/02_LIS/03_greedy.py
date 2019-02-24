numbers = [12, 49, 20, 4, 25, 2, 14]

# 0번에서 시작해서 증가하는 것 뽑기
result = []
for i in range(0, len(numbers)):
    if len(result) == 0:
        result.append(numbers[i])
print(result)
