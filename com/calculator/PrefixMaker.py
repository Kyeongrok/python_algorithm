statement = "1.8 + (3*2)".replace(" ", "")
print(statement)

def tokenizer(statement):
    arr = []
    accu = ""
    for word in statement:
        if word in "[]{}()+-*/^":
            if accu != "":
                arr.append(accu)
                accu = ""
            arr.append(word)
        else:
            accu = accu + word
    return arr

print(tokenizer(statement))