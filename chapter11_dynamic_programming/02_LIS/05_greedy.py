numbers = [12, 49, 20, 4, 25, 2, 14]

result = []
for j in range(0, len(numbers)):
    for i in range(j, len(numbers)):
        if len(result) == 0:
            result.append(numbers[i])
        elif result[len(result)-1] < numbers[i]:
            result.append(numbers[i])
    print(len(result), result)
    result = []

