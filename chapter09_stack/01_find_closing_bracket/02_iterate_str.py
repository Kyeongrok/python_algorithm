def findClosingBracketIndex(str, openIndex):
    stack = []
    for index in range(openIndex, len(str)):
        print(str[index])

    return -1
string = "[[34]HELLO[74]]"
print(findClosingBracketIndex(string, 0))

