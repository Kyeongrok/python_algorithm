def highFrequencyLetterCount(word):
    map = {}
    for alphabet in word:
        if map.get(alphabet) == None:
            map[alphabet] = 1
        print("map=>", map)
    return -1

word = "test"
print(highFrequencyLetterCount(word))
