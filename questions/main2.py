def solution(array):
    different = 0
    sorted_array = sorted(array)

    for i in range(0, len(array)):
        if(array[i] != sorted_array[i]):
            different += 1

    if(different == 2):
        result = True
    else:
        result = False

    return result

if __name__ == "__main__":
    array = [2, 8, 7, 7, 8, 8, 8, 8, 5, 8, 8, 13, 15]
    print("%s %r" % ('The answer is', solution(array)))