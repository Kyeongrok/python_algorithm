list = [3, 8, 9, 6, 2]

def get_max(list):
    box = list[0]
    for num in list:
        if box < num:
            box = num
    return box

print(get_max(list))