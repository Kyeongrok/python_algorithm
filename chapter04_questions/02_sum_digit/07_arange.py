num = 687
def sum(num):
    result = 0
    num = num // 10
    result = result + num % 10
    print("quo:",num, "res:",result)

    while(num > 0):
        result = result + num % 10
        num = num // 10
        print("quo:",num, "res:",result)

    return result

print(sum(num))
