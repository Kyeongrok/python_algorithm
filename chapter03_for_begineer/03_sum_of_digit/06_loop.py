def sum(num):
    result = 0
    quotient = num

    while(quotient > 0):
        remainder = quotient % 10 # 나머지 구하기
        result += remainder # 나머지를 result에 누적
        quotient = quotient // 10 # 몫을 저장
        print("quo:",quotient, "result:",result)
    return result

num = 687
print(sum(num))
