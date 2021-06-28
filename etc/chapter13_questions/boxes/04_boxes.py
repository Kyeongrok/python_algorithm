def boxCount(arr, box_size):
    result = 0
    remainSpaceBoxMap = {}
    for num in arr:
        if num == box_size:
            result += 1
        elif num < box_size:
            if remainSpaceBoxMap.get(num) == None:
                remainSpaceBoxMap[num] = 1

            print(num)
        # box에는 최대 2개까지만 넣을 수 있다.
        # box가 없으면 박스를 하나 만든다.
        # 공간이 차면 없앤다.
        # 공간이 있으면 얼마나 있는지 남겨둔다.
        # 박스는 필요하면 만든다.
        ## 가장 큰 수는 어차피 박스를 한개 먹는다.

        ### 남은 공간이 무게인 map을 찾아보고 있으면 없으면 만들고
        ### 있으면 넣어본다.
    return -1

arr = [1, 2, 3, 1, 2, 2, 3, 1] # 5개
arr = [1, 1, 1, 2, 2, 2, 3, 3]
arr = [2, 3, 3, 3] # 4개
arr = [1, 3, 3, 3] # 4개
arr = [1, 3, 3, 2] # 3개

max = len(arr)
min = sum(arr, 0) // 3
print(max, min)
