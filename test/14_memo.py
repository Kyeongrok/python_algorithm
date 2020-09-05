def solution(temperatures):
    memo = 0
    duration = 0
    for i in range(len(temperatures)):
        # above
        # above or same
        print(temperatures)
        if temperatures[i] > 37 and temperatures[i-1] < temperatures[i]:
            duration += 1
        else:
            duration = 0

        if duration >= 3:
            memo += 1
    return memo


T = [36.7, 36.8, 36.5, 37.1, 37.3, 37.4, 37.2, 36.9, 37.2, 37.3, 37.4, 37.1, 36.7, 36.8, 36.9]
print(solution(T))