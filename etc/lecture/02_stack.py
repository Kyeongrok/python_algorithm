# ) 닫는 bracket이 나올때 까지 stack에 넣는다.
def solution(s):
    answer = True
    list = []
    stack = []
    for c in s:
        list.append(c)
    print(list)



    print(stack)
    return True

solution('()()')
solution(')()(')