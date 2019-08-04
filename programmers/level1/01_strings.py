def solution(strings, n):
    list = []
    aa = sorted(strings, key=lambda str: str[n:len(str)])
    return aa

strings = ["aaa", "abce", "abcd", "cdx", "aae", "aab", "bbb", "bbbb"]

result = solution(strings, 2)
print(result)


