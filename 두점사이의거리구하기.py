import math

채연 = (0, 0)
나영 = (2, 2)

def get두점사이거리(점1, 점2):
    x축거리 = 나영[0] - 채연[0]
    y축거리 = 나영[1] - 채연[1]

    x축거리plusy축거리 = math.pow(x축거리, 2) \
                   + math.pow(y축거리, 2)

    return math.sqrt(x축거리plusy축거리)

result = get두점사이거리(채연, 나영)
print("채연이와 나영이의 거리는:", result)
print("a와 b의 거리는:", get두점사이거리((1, 2), (3, 4)))
print("a와 b의 거리는:", get두점사이거리((3, 4), (1, 2)))


