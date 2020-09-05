# 1 1 2 3 5
num1 = 1
num2 = 1
print(num1)
print(num2)

for i in range(10):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3

