string = "13+3*{24*(35-46.76)-89}"

def stringTokenizer(string):
    # ["1", "+", "2", "*", "(", "3", "-", "4", ")"]
    # [13, +, 24, *, (, 35, -, 46.76, )]
    result = []
    accu = ""
    for chr in string:
        if chr in "+-*/(){}[]^":
            result.append(chr)

    return result   # [ "1", "3", "+", "2", "4" ... ]

result = stringTokenizer(string)
print("=>", result) # [ +, *, - ]
