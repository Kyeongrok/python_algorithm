arr = [7, 3, 2, 9]
def sum(arr):
    last = arr.pop()
    result = last
    last = arr.pop()
    result = result + last
    last = arr.pop()
    result = result + last
    last = arr.pop()
    result = result + last
    return result

result = sum(arr)
print("result=>",result)
