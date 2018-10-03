def sum(accu, arr):
    if len(arr) > 1:
        return sum(accu + arr.pop(), arr)
    else:
        return accu + arr.pop()

arr = [1, 2, 3]
print("result:", sum(0, arr))

