arr = [1, 2, 3, 2, 3, 1, 3]

def getCounter(arr):
    utilMap = {}
    for item in arr:
        if utilMap.get(item) == None:
            utilMap[item] = 1
        else:
            utilMap[item] += 1
    return utilMap

def findOccuringOdd(arr):
    utilMap = getCounter(arr)
    for item in utilMap:
        if utilMap[item] % 2 != 0:
            return item

print(findOccuringOdd(arr))

