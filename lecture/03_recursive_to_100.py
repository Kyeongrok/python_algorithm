# 1번부터 100번까지 루프를 쓰지말고 출력해보세요
def printNumber(num):
    if num > 100: exit()
    print(num)
    return printNumber(num + 1)
printNumber(1)
