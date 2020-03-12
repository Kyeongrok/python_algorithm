list = [3, 8, 9, 6, 2]

def get_min(list):
    result = list[0]
    for i in range(len(list)):
        result = list[i]
    return result

print(get_min(list))