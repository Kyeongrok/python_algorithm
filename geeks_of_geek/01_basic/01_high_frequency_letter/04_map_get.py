def highFrequencyLetterCount(word):
    map = {}
    for alphabet in word:
        if map.get(alphabet) == None:
            print("alphabet=>", alphabet)
        print("map=>", map)
    return -1

word = "test"
print(highFrequencyLetterCount(word))
