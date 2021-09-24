string = 'out of sight, out of mind'
count_each = [0] * 26
for char in string:
    if char.isalpha() == True:
        count_each[ord(char) - 97] += 1

max = 0
for num in count_each:
    if max < num:
        max = num
print(max)