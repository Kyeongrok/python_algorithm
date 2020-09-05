import re

def trajectory(s):
    result = [(0, 0)]
    splitted = re.split('(\d+)', s)
    x_location = 0
    y_location = 0

    for i in range(1, len(splitted), 2):
        if splitted[i-1] == 'U':
            y_location += int(splitted[i])
        elif splitted[i-1] == 'D':
            y_location -= int(splitted[i])
        elif splitted[i-1] == 'R':
            x_location += int(splitted[i])
        elif splitted[i-1] == 'L':
            x_location -= int(splitted[i])

        loc = (x_location, y_location)
        result.append(loc)

    return result

cmd = "U2L4U6D8R12D3"

print(trajectory(cmd))