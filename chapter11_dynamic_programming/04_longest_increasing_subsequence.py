numbers = [10, 22, 9, 33, 21, 50, 41, 60, 80]
numbers2 = [50, 3, 10, 7, 40, 80]

def lis(numbers):
    memoList = [1 for _ in range(len(numbers))]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j] and memoList[i] + 1 > memoList[j]:
                memoList[j] = memoList[i] + 1
            print("j:{} {}".format(j, memoList))
    print(memoList)
    return max(memoList)

print(lis(numbers))
print(lis(numbers2))
