import math
arr = list(range(1, 54))

def sieveMultipleN(arr, diviser, last):
    result = []
    for number in arr:
        if number == diviser or number % diviser != 0:
            result.append(number)

    if diviser == last:
        return result
    else:
        return sieveMultipleN(result, diviser + 1, last)

res = sieveMultipleN(arr, 2,int(math.sqrt(len(arr))))
print(res)
