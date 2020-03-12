string = 'out of sight, out of mind'
count_each = [0] * 26
for char in string:
    if char.isalpha() == True:
        count_each[ord(char) - 97] += 1

max = 0
index = 0
for i in range(len(count_each)):
    if max < count_each[i]:
        max = count_each[i]
        index = i
print(max, chr(index + 97))