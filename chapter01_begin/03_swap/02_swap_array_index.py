list = [1, 2, 3]
print("before:", list)

temp = list[0]
list[0] = list[1]
list[1] = temp

print("after:", list)