list = [1, 2, 3]
print("before:", list)

list[0] = list[1]
list[1] = list[0]

print("after:", list)