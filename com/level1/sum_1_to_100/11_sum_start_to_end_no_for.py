# for문 쓰지 말고 해보세요
def sum_start_to_end(start, end, accu):

    sum_start_to_end(start, end, accu + start + 1)

    return accu

print("result:", sum_start_to_end(1, 100, 0))
