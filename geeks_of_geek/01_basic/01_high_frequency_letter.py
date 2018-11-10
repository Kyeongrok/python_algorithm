word = "test"
# 가장 많이 등장하는 알파벳 찾기
def highFrequencyTimes(word):
    map = {}
    for chr in word:
        if map.get(chr) == None:
            map[chr] = 1
        else:
            map[chr] = map[chr] + 1

    max = 0
    for item in map:
        if max < map[item]:
            max = map[item]
    print(max)

highFrequencyTimes(word)
