
def name_hash(name):
    ascii_sum = 0

    for c in name:
        ascii_sum += ord(c)
    return ascii_sum

print(name_hash('hyunjun'))
print(name_hash('junhyun'))


intDict = {}
for i in range(1000000000000):
    print(i)
    intDict[str(i)] = i

# 해시 테이블
print(intDict['299999999999999'])

