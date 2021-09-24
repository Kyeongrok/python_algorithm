def simplify(str):
    stack = []
    result = ""
    for chr in str:
        if(chr == "+"):
            result = result + chr
        elif(chr == "-"):
            result = result + chr
        elif(chr == "("):
            if(len(result) > 0):
                if(result[len(result)-1] == "+"):
                    stack.append(0)
                else:
                    stack.append(1)
        elif(chr == ")"):
            if(len(stack) > 0):
                stack.pop()
        else:
            result = result + chr
        print("chapter05_stack:", stack)
    return result

statement1 = "a-(b+c)"
statement2 = "(a-b)-(c+d)" #a-b-c-d
statement3 = "a+b-((c+d)-(e-f))"

print(simplify(statement1))
print(simplify(statement2))
