list = [9, 22, 3, 7, 4, 5]
# O(n)
def solution(list):
    result = list[0]
    for num in list[1:]:
        if result < num: # 5번
            result = num
    return result

def solution2(list):
    result = list[0]
    for i in range(1, len(list)):
        if result < list[i]:
            result = list[i]
    return result

# max
# print('=>', solution(list))
print('=>', solution2(list))
