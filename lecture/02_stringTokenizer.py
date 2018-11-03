string = "13+3*{24*(35-46.76)-89}"

def stringTokenizer(string, deli):
    result = []
    accu = ""
    for chr in string:
        if chr in deli:
            if accu != "":
                result.append(accu)
                accu = ""
            result.append(chr)
        else:
            accu = accu + chr

    return result

result = stringTokenizer(string,"+-*/(){}[]^")
print("=>", result) # [ 13, +, 3, *, {, 24 ]
