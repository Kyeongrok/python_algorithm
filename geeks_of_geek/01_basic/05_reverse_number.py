num = 12345

def reverseNumber(num):
    result = 0
    while(num != 0):
        result = (result * 10) + num % 10
        num = num // 10
    return result

print(reverseNumber(num))

