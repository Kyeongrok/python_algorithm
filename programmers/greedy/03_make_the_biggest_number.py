from random import randint
import numpy as np

def solution(number, k):
    remain = number

    i = 1;
    while k > 0:
        if int(remain[i-1]) < int(remain[i]):
            remain = remain[:i-1] + remain[i:]
            k -= 1
        elif int(remain[i]) < int(remain[i+1]):
            remain = remain[:i] + remain[i+1:]
            k -= 1
        elif int(remain[i-1]) == int(remain[i]) and int(remain[i]) == int(remain[i+1]):
            remain = remain[:i] + remain[i+1:]
            k -= 1
        else:
            i += 1
    return str(remain)


print(solution("1924", 2) == "94")
print(solution("1111111119",9) == '9')
print(solution("1231234",3) == '3234')
print(solution('4177252841',4) == '775841')
print(solution('417792252289841',4) == '92252289841')
