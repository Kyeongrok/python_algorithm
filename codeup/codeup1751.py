# 공백을 포함하여 한줄로 된 문자열이 입력된다. 공백을 포함한 길이(문자의 개수)를 출력하시오.

cnt = int(input())
for i in range(cnt):
    line = list(input())
    while(len(line) > 0):
        print(line.pop(), end='')
    print()
