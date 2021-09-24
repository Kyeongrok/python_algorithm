string = 'out of sight, out of mind'
dict = {}
for char in string:
    if dict.get(char) == None:
        dict[char] = 1
    else:
        dict[char] = dict[char] + 1
print(dict)

