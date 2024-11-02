s_nums = input().split(" ")
height = float(s_nums[0])
weight = float(s_nums[1])

get_std_weight = lambda length: (length - 100) * 0.9
get_fat_ratio = lambda real_weight, p_std_weight: (real_weight - p_std_weight)  * 100 / p_std_weight

std_weight = get_std_weight(height)

result = get_fat_ratio(weight, std_weight)

if result <= 10:
    print("정상")
elif result > 10 and result <= 20:
    print("과체중")
elif result > 20:
    print("비만")

# print(height, weight, std_weight, result)
