l1 = []
for i in range(10000):
    l1.append(i)

print(l1)
print(l1[-1], l1[len(l1) - 1])

for i in range(10000):
    l1[i] = l1[i] * 10
print(l1)
print(l1[-1])