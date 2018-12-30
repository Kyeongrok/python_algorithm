input = "nice to meet you"

def reverse(string):
    words = string.split(" ")

    if(len(words) == 2):
        return string

    # 1 to n -1
    print(words)
    return ""

print(reverse(input))
