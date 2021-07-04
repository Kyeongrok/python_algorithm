N = 4

def dfs(arr, depth):
    if depth >= N:
        for i in range(0, N+1):
            print(arr[i], end='')
        print('')
        return ''

    for i in range(1, 9 + 1):
        arr[depth] = i
        print(arr)
        dfs(arr, depth + 1)

dfs([0] * 5, 0)
