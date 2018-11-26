number = 687
def sumOfDigit(num):
    sum = 0

    # 몫, 나머지
    # 홀수, 짝수 2로 나눈 나머지
    quotient = num // 10
    remainder = num % 10
    print(quotient, remainder)
    return sum

print(sumOfDigit(number))