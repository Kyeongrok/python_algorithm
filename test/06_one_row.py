n = 8
rows = [
    [0, 0.5, 0.5, 0, 0, 0, 0, 0],
    [0.5,0,0,0,0.5,0,0,0]
]

for row in rows:
    rowG = []
    theta = 0.85

    for item in row:
        result = item * theta + (1-theta)/n
        rowG.append(result)
    print(rowG)
    print(sum(rowG))

