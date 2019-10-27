import random
pages = [
    {"link":[1, 2], "count":0},
    {"link":[0, 4], "count":0},
    {"link":[1, 7], "count":0},
    {"link": [2], "count":0},
    {"link": [3, 7], "count":0},
    {"link": [3, 4], "count":0},
    {"link": [3, 5], "count":0},
    {"link": [0, 3, 6], "count":0}
]

for i in range(10000):
    pageNo = random.randint(0, 7)
    n = len(pages[pageNo]["link"])

    arIdx = random.randint(0, n -1)
    rnd = random.random()

    toPageIdx = pages[pageNo]["link"][arIdx]
    if rnd < 1 / n :
        toPageIdx = pageNo
    # print(pageNo, toPageIdx)
    pages[toPageIdx]["count"] += 1

print(pages)

sum = 0
for page in pages:
    sum += page["count"]
    print(page["count"])
