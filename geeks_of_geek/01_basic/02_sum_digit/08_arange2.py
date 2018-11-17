def sum(num):
    result = 0
    while(num > 0):
        result = result + num % 10
        num = num // 10
    return result

print(sum(6879))
