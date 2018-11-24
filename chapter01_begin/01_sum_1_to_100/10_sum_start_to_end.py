# 변수 쓰지 말고 해보세요
# 지역(local) 변수 안쓰고요? 네
def sum_start_to_end(start, end, accu):
    for num in range(start, end + 1):
        accu = accu + num

    return accu

print("result:", sum_start_to_end(1, 100, 0))
