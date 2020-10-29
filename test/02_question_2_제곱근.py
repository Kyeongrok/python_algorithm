# root = i * i
# i ^ 2 = N
# i^2 - N = 0

# 100 -> 10
# 25 -> 5

def solution(n):
    # n의 제곱근이 x라고 한다.
    # 100
    # 50
    # 25
    # 12.5
    # 10 -----> 제곱근
    # 6.125
    # 계산한 수가 n보다 작은지 본다.
    x = n
    left = 0  # 작은 쪽
    right = n  # 큰 쪽
    # x * x가 n보다 작은 값이 나왔으면 그 값보다는 큰 값으로 검색 해본다.
    # 12.5 의 제곱이 100보다 크다
    # 6.25의 제곱은 100보다 작다
    # 12.5와 6.25의 중간값을 x로 한다.
    for i in range(10):
        x = (left + right) / 2 # 50
        # x로 구한 값이 n(100)보다 작으면 잘못 구한 것이다.
        # 그러니 더 작은 값으로 x * x < n인지 시도 해본다.
        print(x)
        # x * x가 100보다 작다는 것은 left를 x로
        if x * x < n:
            # 계속 한다.
            left = x
        else:
            right = x
        # 1부터 n까지 숫자를 검색 했을 때 n이 x에 가까워지는 방법
        print('left:{}, right:{}'.format(left, right))
    return x

# print(solution(100) == 10)
# print(solution(25) == 5)
solution(0.01)




