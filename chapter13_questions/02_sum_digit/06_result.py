num = 687
def sum(num):
    result = 0
    quotient = num // 10
    remainder = num % 10
    result = result + remainder
    print("quo:",quotient, "re:",remainder)

    while(quotient > 0):
        remainder = quotient % 10
        quotient = quotient // 10
        result = result + remainder
        print("quo:",quotient, "re:",remainder)

    return result

print(sum(num))
