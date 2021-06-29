def perm(input, i):
    if i == len(input) - 1:
        print(input)
    else:
        for j in range(i, len(input)):
            input[i], input[j] = input[j], input[i]
            perm(input, i + 1)
            input[i], input[j] = input[j], input[i]

perm(['치과','내과','안과'], 0)
