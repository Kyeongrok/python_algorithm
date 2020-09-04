'''
0 1
0 2
0 3

'''
result = [
]

memo = [(1, 2), (3, 4)]
for i in range(len(memo)):
    list = []
    for j in range(len(memo)):
        list.append(memo[i][0] - memo[j][1])
    result.append(list)

for row in result:
    print(row)