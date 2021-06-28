def sum(quotient): # 파라메터 이름을 바꿈
    result = 0
    while(quotient > 0):
        remainder = quotient % 10
        result += remainder # 나머지를 result에 누적
        quotient = quotient // 10
    return result

num = 687
print(sum(num))
