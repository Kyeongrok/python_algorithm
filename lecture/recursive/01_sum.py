arr = [7, 3, 2, 9, 4]
def sum(arr, accu):
    if(len(arr) == 0): return accu
    return sum(arr, accu + arr.pop())

#탈출조건, 끝나는 조건을 꼭 넣어주어야 합니다.
# return sum(arr, accu + arr.pop())# print("result=>", sum(arr, 0)) # 25
