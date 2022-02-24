# a, 1 입력하면 b
# b, 2 입력하면 d
# z, 1 입력하면 a
def calc_chr(c, n):
    ascii = ord(c)
    theta = 64
    if ascii >= 97:
        theta = 96

    # ascii형으로 변경
    r = (ascii - theta) % 26 + n
    while r > 26: # b 25인 경우 {가 나올 수 있음
        r = r % 26
    return chr(theta + r)

def solution(s, n):
    r = ""
    for c in s:
        if c != ' ':
            r += calc_chr(c, n)
        else:
            r += c
    return r

print(solution("b", 25)) # a

