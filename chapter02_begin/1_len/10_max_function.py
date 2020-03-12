list = [3, 8, 9, 6, 2]

def get_max(list):
    box = None
    for num in list:
        if box < num:
            box = num
    return box

print(get_max(list))
# print(max([]))