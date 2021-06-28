
def get_another_box_name(boxName):
    if boxName == "A":
        return "B"
    else:
        return "A"


def solution(from_box, ball, num_A, num_B):
    box_map = {"A":num_A, "B":num_B}

    for i in range(len(from_box)):
        box_name = from_box[i]
        target_box_name = get_another_box_name(box_name)
        target_box_ball_count = box_map[target_box_name]
        diff = ball[i]
        if target_box_ball_count + ball[i] > 1000:
            # 1000이 될때까지만 빼서 더한다
            diff = 1000 - target_box_ball_count

        box_map[box_name] -= diff
        box_map[target_box_name] += diff

    return [box_map["A"], box_map["B"]]

fromBox = ["A", "B"]
ball = [2, 5]
numA = 5
numB = 7

fromBox = ["A", "B", "A", "B"]
ball = [10, 20, 200, 20]
numA = 980
numB = 890

result = solution(fromBox, ball, numA, numB)
print(result)