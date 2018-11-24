numbers = [1, 2, 3, 4, 5, 6, 7]

def multiple2(arr):
    result = []
    for number in arr:
        if number % 2 != 0:
            result.append(number)
    return result

def multiple3(arr):
    result = []
    for number in arr:
        if number % 3 != 0:
            result.append(number)
    return result


result = multiple2(numbers)
result3 = multiple3(numbers)
print(result3)
