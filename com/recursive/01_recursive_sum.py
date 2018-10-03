arr = [1, 2, 3]

def sum(accu, arr):

    if len(arr) > 1:
        popped = arr.pop()
        sum1 = accu + popped
        print("arr:",arr)
        return sum(sum1, arr)
    else:
        return accu + arr.porp()

print("result:", sum(0, arr))

