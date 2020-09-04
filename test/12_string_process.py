def solution(list):
    return sorted(list, key=lambda x: (len(x), x))

w = solution(['Python', 'for', 'data','science', 'quiz', 'date'])
print(w)



