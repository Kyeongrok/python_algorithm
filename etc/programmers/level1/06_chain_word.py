def solution(n, words):
    memo = [words[0]]
    alreadyExist = None
    for i in range(len(words)-1):
        first = words[i]
        second = words[i + 1]
        try:
            alreadyExist = memo.index(second) >= 0
        except:
            alreadyExist = False

        if first[len(first)-1] != second[0] or alreadyExist:
            quote = (i + 2) // n
            remainder = (i + 2) % n
            nThPlayer = remainder
            nThTry = quote + 1
            if remainder == 0:
                nThPlayer = n
                nThTry = quote
            return [nThPlayer, nThTry]
        else:
            memo.append(second)
    return [0, 0]



print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
# print(solution(3, ['tank', 'tank', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
# print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))
# print(solution(2, ['hello', 'nne', 'even', 'never', 'now', 'world', 'draw']))
# 2, 1이렇게 나와야 대눈데
