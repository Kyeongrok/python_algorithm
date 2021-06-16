arr = [7, 3, 2, 9]
def sum(arr, accu):
    if(len(arr) == 0): return accu
    return sum(arr, accu + arr.pop())

print("result=>",sum(arr, 0))