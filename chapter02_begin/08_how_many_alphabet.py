string = 'out of sight, out of mind'
dict = {}
for char in string:
    if dict.get(char) == None:
        print("-----True-----")