def solution(n,a,b):
    count = 0
    arr = [0] * n
    arr[a-1] = 1
    arr[b-1] = 1
    result = []
    while(len(arr) >= 2):
        count += 1
        for i in range(0, len(arr), 2):
            print(i)
            if(arr[i] > arr[i+1]):
                result.append(arr[i])
            elif(arr[i] <= arr[i+1]):
                result.append(arr[i+1])
            elif(arr[i] == 1 and arr[i+1] == 1):
                return count
            else:
                print("------")
        arr = result
        result = []
    return count
aa = solution(16, 4, 15)
print(aa)
