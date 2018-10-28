arr = [7, 3, 2, 9]
def sum(arr):
    print(arr)
    last = arr.pop()
    result = last
    return sum(arr)

result = sum(arr)
print("result=>",result)