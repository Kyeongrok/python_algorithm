
def solution(array):
    result = 0
    head_cnt = 0
    tail_cnt = 0
    for i in array:
        if(i == 0):
            head_cnt += 1
        elif(i == 1):
            tail_cnt += 1

    if(head_cnt > tail_cnt):
        result = tail_cnt
    elif(head_cnt <= tail_cnt):
        result = head_cnt

    return result


if __name__ == "__main__":
    array = [1, 1, 0, 1, 1, 1]
    print("%s %d" % ('The answer is', solution(array)))