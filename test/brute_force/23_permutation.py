def factorial(lst):
    n = len(lst)
    ret = []
    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])

    # A를 뽑았으면 남은 것을 가지고 돌립니다.
    elif n > 1:
        for i in range(len(lst)): # lst에 값이 3개라면 총 3번을 반복합니다.
            temp = [i for i in lst]
            temp.remove(lst[i]) # i번째는 지웁니다. 왜냐하면 값을 뽑았기 때문입니다.
            print(f'temp:{temp}')
            per_res = factorial(temp) # 여기는 재귀를 썼음 i번째를 지운 list를 넘깁니다
            for p in per_res:
                print(f'p:{p}')
                ret.append([lst[i]] + p) # 기존 lst에 p를 합칩니다.

    print(f'ret:{ret}')
    return ret

print(factorial(['A', 'B', 'C']))