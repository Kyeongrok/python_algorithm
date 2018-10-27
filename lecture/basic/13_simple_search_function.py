arr = [3, 4, 8, 9, 7]

# 찾는 숫자가 있으면 index를 리턴
# 없으면 -1

def simpleSearch(arr, num):
    # 몇번째 인덱스에 있는지 return하는 함수
    for index in range(0, len(arr)):
        if arr[index] == num:
            return index
    return -1

result = simpleSearch(arr, 7)
print("result=>", result) # 2

# len(arr) = 1 => 1
# len(arr) = 10 => 10
# len(arr) = 100 => 100
# len(arr) = 1000 => 1000
# len(arr) = 1000000 => 1000000
# len(arr) = 100000000 => 100000000
# O(n)
