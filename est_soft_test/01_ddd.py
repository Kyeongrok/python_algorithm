def solution(arr1, arr2):
    # 3 * 2행렬
    answer = [ [-1] * len(arr2[0]) for _ in range(len(arr1))]

    arr1_column_cnt = len(arr1[0])

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            answer[i][j] = 0
            for i_col in range(arr1_column_cnt):
                answer[i][j] += arr1[i][i_col] * arr2[i_col][j]
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]


print(solution(arr1, arr2))
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]


print(solution(arr1, arr2))
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4], [3, 1, 4]]
arr2 = [[5, 4, 3, 5], [2, 4, 1, 5], [3, 1, 1, 7]]

print(solution(arr1, arr2))

arr1 = [[2, 3, 2], [4, 2, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]
print(solution(arr1, arr2))