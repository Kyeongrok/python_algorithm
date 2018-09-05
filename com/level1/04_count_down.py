# recursive
def count_down(num):
    # 현재 숫자를 출력한다
    # 한개 줄여서 자신을 다시 호출한다.
    # 0이 되면 멈춘다.
    if(num == 0):
        print(num)
    else:
        print(num)
        count_down(num - 1)

count_down(10)