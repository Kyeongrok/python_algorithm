def getSetNum(array):
    return len(set(array))

def solution(array):
    init_num = getSetNum(array)
    min = len(array)

    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if(i < j):
                if(init_num == getSetNum(array[i:j])):
                    if(min > j - i):
                        min = j - i

    result = min
    return result

if __name__ == "__main__":
    array1 = [2, 1, 1, 3, 2, 1, 1, 3]
    array2 = [7, 5, 2, 7, 2, 7, 4, 7]
    print("%s %r" % ('The answer is', solution(array2)))