numbers = [1, 2, 4, 3, 5]
memo = [1] * len(numbers)

for i in range(1, len(numbers)):
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            print("numbers[j]:", numbers[j],"<" ,"numbers[i]:", numbers[i])
