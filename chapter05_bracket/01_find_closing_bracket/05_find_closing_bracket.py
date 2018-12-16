def findClosingBracketIndex(str, openIndex):
    stack = []
    for index in range(openIndex, len(str)):
        char = str[index]
        if(str[index] == "["):
            stack.append(char)
        elif(char == "]"):
            # stack이 0보다 크면 stack에서 pop한다.
            stack.pop()

        # stack에 아무것도 없으면 index를 return한다.
        if(not stack):
            return index
    return -1
string = "[[34]HELLO[74]]"
print(findClosingBracketIndex(string, 1))

