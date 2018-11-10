word = "elegance"
def highFrequencyLetterCount(word):
    map = {}
    for alphabet in word:
        if map.get(alphabet) == None:
            map[alphabet] = 1
        else:
            map[alphabet] += 1

    max = -1
    for key in map:
        if map[key] > max:
            max = map[key]

    return max

print("result=>", highFrequencyLetterCount(word))