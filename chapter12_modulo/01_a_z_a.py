# a, 1 입력하면 b
# b, 2 입력하면 d
# z, 1 입력하면 a
def calc_chr(c, n):
    ascii = ord(c)
    theta = 64
    if ascii >= 97:
        theta = 96

    # ascii형으로 변경
    r = (ord(c) - theta) % 26 + n
    return chr(theta + r)

def solution(s, n):
    r = ""
    for c in s:
        r += calc_chr(c, n)
    return r

print(solution("ABC", 2))