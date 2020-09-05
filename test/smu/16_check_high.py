file = open("./AAPL.csv")

lines = file.readlines()[1:]
parsed_list = []
for i in range(len(lines)):
    line = lines[i]
    spl = line.replace("\n", "").split(",")
    parsed_list.append((float(spl[1]), float(spl[4])))

print(parsed_list)

for i in range(len(parsed_list) - 1):
    # 1번의 open이 0번의 close보다 높으면 buy 출력
    # pass
    today_open = parsed_list[i+1][0]
    yesterday_close = parsed_list[i][1]
    # print(today_open, yesterday_close)
    if today_open > yesterday_close:
        print(today_open, yesterday_close, 'buy')
    else:
        print('not buy')


