number = 687
def sumOfDigit(num):
    sum = 0
    quotient = num // 10
    remainder = num % 10
    sum = sum + remainder

    remainder = quotient % 10
    quotient = quotient // 10
    sum = sum + remainder

    remainder = quotient % 10
    quotient = quotient // 10
    sum = sum + remainder
    print(quotient, remainder, sum)

    return sum

print(sumOfDigit(number))