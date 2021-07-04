joined = ['cat', 'dog', 'elephant', 'lion', 'leopard', 'zebra', 'horse', 'bear']
passed = ['cat', 'dog', 'elephant', 'lion', 'leopard', 'zebra', 'horse']
check = [0 for _ in range(len(joined))]

# Naive
i = 0
for j in joined:
    for p in passed:
        if p == j :
            check[i] += 1
            break
    i += 1

print(check)

for i in range(len(joined)):
    if check[i] == 0 :
        print(joined[i])
        break


# Dictionary
data  = {}
for x in joined :
    data[x] = data.get(x, 0)
    data[x] += 1

for x in passed:
    data[x] -= 1

answer_list = [k for k, v in data.items() if v >0]
answer = answer_list[0]
print(answer)