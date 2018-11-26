number = 687
def sumOfDigit(num):
    sum = 0
    # 몫, 나머지
    # 홀수, 짝수 2로 나눈 나머지
    quotient = num // 10
    remainder = num % 10
    sum = sum + remainder

    print(quotient)
    remainder = quotient % 10
    quotient = quotient // 10
    sum = sum + remainder
    print(quotient, remainder, sum)

    return sum

print(sumOfDigit(number))