from datetime import datetime
intDict = {}
for i in range(0, 30000000):
    intDict[str(i)] =  i

print(datetime.now())
print(intDict["29999999"])
print(datetime.now())