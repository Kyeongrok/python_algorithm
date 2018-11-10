def highFrequencyLetterCount(word):
    map = {}
    for alphabet in word:
        if map.get(alphabet) == None:
            map[alphabet] = 1
        else:
            map[alphabet] += 1

    for key in map:
        print("key=>", key)

    return -1

word = "test"
print(highFrequencyLetterCount(word))
