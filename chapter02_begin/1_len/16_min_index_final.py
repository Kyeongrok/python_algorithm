list = [3, 8, 9, 6, 2]

def get_min(list):
    result = list[0]
    for i in range(1, len(list)):
        if list[i] < result:
            result = list[i]
    return result

print(get_min(list))