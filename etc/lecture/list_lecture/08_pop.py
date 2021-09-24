l1 = []
for i in range(10000):
    l1.append(i)

print(l1)
l1.pop(0)
print(l1)
print(len(l1), l1[-1])

print('.pop()', l1.pop())
print(l1)
print(l1[-1], len(l1))