number = 687
def sumOfDigit(num):
    sum = 0
    while(num > 0):
        remainder = num % 10
        num = num // 10
        sum = sum + remainder
        print("q:", num, "r:", remainder, "sum:",sum)
    return sum

print(sumOfDigit(number))