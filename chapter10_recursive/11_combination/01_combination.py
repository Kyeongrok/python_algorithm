
# for i in range(1, 3 + 1):
#     for j in range(1, 3 + 1):
#         print(i, j)

def printAlphabets(char):
    print(char)
    if char == 'Z':
        return
    printAlphabets(chr(ord(char) + 1))

printAlphabets('A')
