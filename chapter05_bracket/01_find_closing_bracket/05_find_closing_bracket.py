def findClosingBracketIndex(str, openIndex):
    stack = []
    for index in range(openIndex, len(str)):
        if(str[index] == "["):
            stack.append(str[index])
        elif(str[index] == "]"):
            stack.pop()

        # stack에 아무것도 없으면 index를 return한다.
        if(not stack):
            return index
    return -1
string = "[[34]HELLO[74]]"
print(findClosingBracketIndex(string, 1))

