# for문 쓰지 말고 해보세요
def sum_start_to_end(start, end, accu):
    if(start > end):
        return accu
    else:
        return sum_start_to_end(start + 1, end, accu + start)

print("result:", sum_start_to_end(1, 100, 0))
