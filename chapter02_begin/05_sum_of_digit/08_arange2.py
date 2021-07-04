def sum(quotient):
    result = 0
    while(quotient > 0):
        # remainder변수 없애고 바로 result에 더하기
        result = result + quotient % 10
        quotient = quotient // 10
    return result

print(sum(6879))
