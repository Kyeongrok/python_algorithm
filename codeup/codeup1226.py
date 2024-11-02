numbers1 = input().split(' ')
numbers2 = input().split(' ')
# numbers1 = '13 23 24 35 40 45 7'.split(' ')
# numbers2 = '2 6 7 23 40 44'.split(' ')

converter_s_to_n = lambda s_nums: [int(s_nums[i]) for i in range(len(s_nums))]

i_nums1 = converter_s_to_n(numbers1)
i_nums2 = converter_s_to_n(numbers2)


def lotto(i_nums1, i_nums2):
    bonus_num = i_nums1[-1]
    memo = [0] * 46
    for i in range(6):
        v = i_nums1[i]
        memo[v] = 1

    cnt = 0
    for i in range(6):
        v = i_nums2[i]
        if memo[v] == 1:
            # print(v, memo[v])
            cnt += 1

    # print(cnt)


    # 5 개가 맞은 경우
    if cnt == 6:
        return 1
    elif cnt == 5:
        for num in i_nums2:
            if num == bonus_num:
                return 2
        return 3
    elif cnt <= 2:
        return 0
    elif cnt == 4:
        return 4
    elif cnt == 3:
        return 5


result = lotto(i_nums1,i_nums2)
print(result)

