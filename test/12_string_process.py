# 길이 오름 차순 정렬하기
def solution(list):
    return sorted(list, key=lambda x: (len(x), x))

w = solution(['Python', 'for', 'data','science', 'quiz', 'date'])
print(w)



