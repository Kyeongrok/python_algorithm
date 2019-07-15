list = [9, 7, 40, 19, 4, 2]

# 두가지가 있다. first를 뽑을 것인지 last를 뽑을 것인지
# 정하는 방법은 상대방이 뽑을 두번째를 보고 고를 수 있다.

# 상대방이 무엇을 뽑게 할 것인지 정할 수 있다.

# 다음에 뽑는 것의 max가 결과의 max인가?
# 1, 2뽑는 것의 max가 되는 값을 선택 한다.

#경우의 수
# 9 4 40 : 2 19 7
# 2   : 4

first = list[0]
last = list[len(list)-1]

aPick = []
bPick = []

if(first > last):
    aPick.append(list.pop())
print()

maxValueSum = 0
