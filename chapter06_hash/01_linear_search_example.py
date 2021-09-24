from datetime import datetime
intList = range(0, 30000000)

print(datetime.now())
for i in intList:
    if(i == 29999999) :
        print(i)
        break
print(datetime.now())


