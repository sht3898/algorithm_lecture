import sys; sys.stdin = open('4875_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global result
    visited[x][y] = 1
    if arr[x][y] == 3:
        result = 1
        return
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
            dfs(nx, ny)


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_x, start_y = i, j
    dfs(start_x, start_y)
    print('#{}'.format(TC), end=' ')
    print(result)
