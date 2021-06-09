def sumOfDigit(num):
    sum = 0
    while(num > 0):
        remainder = num % 10
        num = num // 10
        sum = sum + remainder
    return sum

print(sumOfDigit(687))
print(sumOfDigit(7986))
print(sumOfDigit(111111122322112))
print(sumOfDigit(0))
print(sumOfDigit(1))
