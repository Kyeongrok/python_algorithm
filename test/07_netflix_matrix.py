matrix = [
    [5, 4, 4, 0, 5],
    [0,3,5,3,4],
    [5,2,0,2,3],
    [0,2,3,1,2],
    [4,0,5,4,5],
    [5,3,0,3,5],
    [3,2,3,2,0],
    [5,3,4,0,5],
    [4,2,5,4,0],
    [5,0,5,3,4]
]

편차 = []

sum1 = 0
for i in range(len(matrix)):
    for j in range(5):
        sum1 += matrix[i][j]
avg = sum1 / 10 / 5
print(avg)

#sig (평균 - 값)^2 / 10
sum3 = 0
for i in range(len(matrix)):
    row = []
    for j in range(5):
        ext = avg - matrix[i][j]
        row.append(pow(ext, 2))
    sum2 = sum(row)
    sum3 += sum2
print(sum3 / 10 / 5)
