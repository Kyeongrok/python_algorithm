arr = [7, 3, 2, 9]

def sum(arr):
    last = arr.pop()
    print(last)
    result = arr[0] + arr[1] + arr[2] + arr[3]
    print(result)

result = sum(arr)
print(result)