# pow(2, 3) = 8

def pow(num, power):
    if power == 0: return 1

    result = num
    while(power > 1):
        result = result * num
        power = power - 1

    return result

print(pow(2, 0))
print(pow(7, 2))
