arr = [7, 3, 2, 9]

def sum(arr):
    last = arr.pop()
    print("arr=>", arr)
    print("last=>", last)
    result = arr[0] + arr[1] + last # 7, 3, 9

    # arr = [7, 3, 2]
    last = arr.pop() # 2
    print("arr2=>", arr)
    print("last2=>", last)
    result = result + last

    return result

result = sum(arr)
print("result=>",result)
