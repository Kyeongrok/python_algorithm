list = [
    {"Name":"aaaa", "Id":1, "Subject":"Science", "Score":80},
    {"Name":"aaaa", "Id":1, "Subject":"Math", "Score":90},
    {"Name":"bbb", "Id":2, "Subject":"Science", "Score":70},
    {"Name":"ccc", "Id":3, "Subject":"Science", "Score":60},
]

student_map = {}

for score in list:
    if student_map.get(score['Id']) == None:
        student_map[score['Id']] = []
    student_map[score['Id']].append(score)

def avg(list):
    total = 0
    for item in list:
        total += item['Score']
    return total / len(list)

for k, v in student_map.items():
    print('name:{} id:{} avg:{} count:{}'.format(
        v[0]['Name'], k, avg(v), len(v)))

print(student_map)