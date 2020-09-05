numbers = [8, 5, 9, 10]

middle = len(numbers) // 2
left = sorted(numbers[0:middle])
right = sorted(numbers[middle:len(numbers)])
sorted_arr = []

pointer_left, pointer_right = 0, 0
while pointer_left < len(left) and pointer_left < len(right):
    if left[pointer_left] <= right[pointer_right]:
        sorted_arr.append(left[pointer_left])
        pointer_left += 1
    else:
        sorted_arr.append(right[pointer_right])
        pointer_right += 1

if pointer_left == len(left):
    sorted_arr.extend(right[pointer_right:])
else:
    sorted_arr.extend(left[pointer_left:])
print(sorted_arr)

