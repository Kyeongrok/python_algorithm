arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

def getOccuringOdd(arr):
    res = 0
    for item in arr:
        res = res ^ item
    return res
print(getOccuringOdd(arr))

