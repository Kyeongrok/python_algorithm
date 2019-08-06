def solution(s):
    answer = ''
    sizeRemainder = len(s) % 2
    if sizeRemainder == 0:
        #짝수
        return s[sizeRemainder-1] + s[sizeRemainder]
    else:
        return s[sizeRemainder]