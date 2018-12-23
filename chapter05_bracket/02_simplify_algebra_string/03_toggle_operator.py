def simplify(str):
    stack = []
    result = ""
    for chr in str:
        if(chr == "+"):
            if(len(stack) > 0 and stack[len(stack)-1] == 1):
                result = result + "-"
            else:
                result = result + "+"
        elif(chr == "-"):
            if(len(stack) > 0 and stack[len(stack)-1] == 1):
                result = result + "+"
            else:
                result = result + "-"
        elif(chr == "("):
            if(len(result) > 0):
                if(result[len(result)-1] == "+"):
                    stack.append(0)
                else:
                    stack.append(1)
        elif(chr == ")" ):
            if(len(stack) > 0):
                stack.pop()
        else:
            result = result + chr
    return result

statement1 = "a-(b+c)"
statement2 = "(a-b)-(c+d)" #a-b-c-d
statement3 = "a+b-((c+d)-(e-f))" #a+b-c-d+e-f

print(simplify(statement1))
print(simplify(statement2))
print(simplify(statement3))
