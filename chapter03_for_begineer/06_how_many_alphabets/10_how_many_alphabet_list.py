string = 'out of sight, out of mind'
count_each = [0] * 26

for char in string:
    if char.isalpha() == True:
        print('------ isalpha ----')