# for문 쓰지 말고 해보세요
def sum_start_to_end(start, end, accu):

    if(start < end):
        sum_start_to_end(start + 1, end, accu + start)

    return accu

print("result:", sum_start_to_end(1, 100, 0))
