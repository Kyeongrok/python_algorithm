from random import randint
import numpy as np

def solution(number, k):
    remain = number

    for _ in range(k):
        i = 1;
        while i < len(remain)-1:
            # print(i, remain)
            before = int(remain[i-1])
            here = int(remain[i])
            next = int(remain[i+1])
            if  before < here:
                remain = remain[:i-1] + remain[i:]
            elif before > here:
                remain = remain[:i] + remain[i+1:]
            elif here < next:
                remain = remain[:i] + remain[i+1:]
            elif int(remain[i-1]) == int(remain[i]) and int(remain[i]) == int(remain[i+1]):
                remain = remain[:i] + remain[i+1:]
            i+=1
            print(remain, len(remain), k, i)
    return str(remain)


# print(solution("1924", 2) == "94")
print(solution("1111111119",9) == '9')
# print(solution("9111111111",9) == '9')
# print(solution("9117711111",9) == '9')
# print(solution("1231234",3) == '3234')
# print(solution('4177252841',4) == '775841')
# print(solution('417792252289841',4) == '92252289841')
