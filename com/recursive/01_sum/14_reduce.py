arr = [7, 3, 2, 9]

def sum(arr, accu):
    print(arr, accu)
    if(len(arr) == 0): return accu
    last = arr.pop()
    return sum(arr, accu + last)

result = sum(arr, 0)
print("result=>",result)
