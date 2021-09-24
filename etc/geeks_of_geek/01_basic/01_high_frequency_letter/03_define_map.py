def highFrequencyLetterCount(word):
    map = {}
    for alphabet in word:
        if map[alphabet] == None:
            print("alphabet=>", alphabet)
    return -1

word = "test"
print(highFrequencyLetterCount(word))
