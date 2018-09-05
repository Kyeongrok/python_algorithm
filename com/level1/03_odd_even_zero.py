def odd_even_zero(num):
    if(num == 0):
        return "zero"
    elif(num % 2 != 0):
        return "even"
    elif(num % 2 == 0):
        return "odd"

for num in range(0, 10):
    print(num, ":", odd_even_zero(num))
