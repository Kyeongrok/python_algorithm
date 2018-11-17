num = 687
def sum(num):
    result = 0
    quotient = num // 10
    result = result + num % 10
    print("quo:",quotient, "res:",result)

    while(quotient > 0):
        result = result + quotient % 10
        quotient = quotient // 10
        print("quo:",quotient, "res:",result)

    return result

print(sum(num))
