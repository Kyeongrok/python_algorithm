import random
names = [
"김경록", "정다은",
"조은진", "김진주",
"이예나", "설창환",
"박송", "박윤준", "조현정"
]

def print_seats(numbers):
    print(names[numbers[0]], names[numbers[1]])
    print(names[numbers[2]], names[numbers[3]])
    print(names[numbers[4]], names[numbers[5]])
    print(names[numbers[6]], names[numbers[7]], names[numbers[8]])

for i in range(23, 41):
    rnd_numbers = random.sample(range(0, 9), 9)
    print("-----{}주차-----".format(i))
    print_seats(rnd_numbers)

