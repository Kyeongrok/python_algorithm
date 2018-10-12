# 바이너리갭 binary gap구하기

def getBinaryNumber(result, num):
    # num이 1보다 작거나 같으면 return
    if num >= 1:
        return getBinaryNumber(str(result) + str(num % 2), num // 2)
    return result


num = 1041
print(getBinaryNumber("", num))