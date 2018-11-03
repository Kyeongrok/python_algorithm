word = "test"

# 개수 세고
#
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
