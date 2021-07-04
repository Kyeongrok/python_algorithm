def dfs(depth):
    if depth == 4:
        print('depth is 4')
        return 'eeee'
    for i in range(1, 6 + 1):
        print(i)
        dfs(i + 1)

dfs(4)
