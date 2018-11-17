num = 687
def sum(num):
    quotient = num // 10
    remainder = num % 10
    print("quo:",quotient, "re:",remainder)

    quotient2 = quotient // 10
    remainder2 = quotient % 10
    print("quo:",quotient2, "re:",remainder2)

print(sum(num))

