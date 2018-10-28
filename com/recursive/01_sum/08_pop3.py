arr = [7, 3, 2, 9]

def sum(arr):
    last = arr.pop()
    print("arr=>", arr)
    print("last=>", last)
    result = arr[0] + last # 7, 3, 9

    # arr = [7, 3, 2]
    last = arr.pop() # 2
    print("arr2=>", arr)
    print("last2=>", last)
    result = result + last

    # arr = [7, 3]
    last = arr.pop()  # 3
    print("arr3=>", arr)
    print("last3=>", last)
    result = result + last

    return result

result = sum(arr)
print("result=>",result)
