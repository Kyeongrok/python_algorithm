list = [3, 8, 9, 5, 4, 2]
# 여기에서 7이 있으면 true 없으면 false를 리턴하는 함수를 만들어보세요.

def findNumber(number):
    for item in list:
        if(item == number):
            return True
    return False

print(findNumber(2))
print(findNumber(7))
