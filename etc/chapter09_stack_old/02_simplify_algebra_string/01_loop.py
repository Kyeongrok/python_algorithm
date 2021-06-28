def simplify(str):
    for chr in str:
        print(chr)
    return ""

statement1 = "a-(b+c)"
statement2 = "(a-b)-(c+d)" #a-b-c-d
statement3 = "a+b-((c+d)-(e-f))"

print(simplify(statement1))