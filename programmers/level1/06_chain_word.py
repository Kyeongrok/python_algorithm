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
            print(first, second, i+2)
            quote = (i + 2) // n
            remainder = n - (i + 2) % n
            return [remainder, quote + 1]
        else:
            memo.append(second)
    return [0, 0]



print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))
