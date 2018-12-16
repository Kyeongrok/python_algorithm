def findClosingBracketIndex(str, openIndex):
    stack = []
    for index in range(openIndex, len(str)):
        if(str[index] == "["):
            stack.append(str[index])
        elif(str[index] == "]"):
            stack.pop()

        print(stack)

    return -1
string = "[[34]HELLO[74]]"
print(findClosingBracketIndex(string, 0))

