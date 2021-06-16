def pic2(arr):
    tuple1 = (arr[0], arr[1])
    tuple2 = (arr[0], arr[2])
    tuple3 = (arr[0], arr[3])

    return [tuple1, tuple2, tuple3]

arr = [1, 2, 3, 4, 5, 6, 7]
print(pic2(arr))

# (1, 2), (1, 3), (1, 4) ....
# (2, 1), (2, 3), (2, 4) ....