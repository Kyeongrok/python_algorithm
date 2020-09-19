l1 = []

for i in range(1000000):
    l1.append(i)

print(l1) # 0, 999999
print(len(l1))
print('l1[1]:', l1[1])
print('end:', l1[len(l1) - 1])