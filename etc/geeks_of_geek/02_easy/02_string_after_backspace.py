str = "###abc#de#f#ghi#jklmn#op#"
result = []

for chr in str:
    if chr == "#":
        if len(result) != 0: result.pop()
    else:
        result.append(chr)
    print(result)
print(result)
