f1 = open("./idlists.txt", mode='r')
lines = [id.replace("\n", "") for id in f1.readlines()]
splitted = [info.split("\t") for info in lines]

score = {

}

for ar in splitted:
    try:
        score[ar[0]] = float(score[ar[0]]) + float(ar[1])
    except:
        score[ar[0]] = float(ar[1])


for item in score:
    print(item, score[item])