arr = [7, 3, 2, 9]

def sum(arr):
    last = arr.pop()
    print("arr=>", arr)
    print("last=>", last)
    result = arr[0] + arr[1] + arr[2] + last
    return result

result = sum(arr)
print("result=>",result)
