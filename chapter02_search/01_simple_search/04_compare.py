arr = [1,2,3,5,6,7,8,9,10,11]

def simpleSearch(arr, targetNum):
    for index in range(0, len(arr)):
        if arr[index] == targetNum:
            return index
    return -1

print(simpleSearch(arr,8))
print(simpleSearch(arr,4))