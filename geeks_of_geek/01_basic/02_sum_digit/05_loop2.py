num = 687
def sum(num):
    quotient = num // 10
    remainder = num % 10
    print("quo:",quotient, "re:",remainder)

    while(quotient > 0):
        remainder = quotient % 10
        quotient = quotient // 10
        print("quo:",quotient, "re:",remainder)

print(sum(num))
