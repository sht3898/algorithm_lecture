import sys; sys.stdin = open('1210_input.txt', 'r')

dx = [-1, 0, 0]
dy = [0, 1, -1]


def dfs(x, y):
    global result
    stack.append((x, y))
    visited[x][y] = 1
    while stack:
        a, b = stack.pop()
        if a == 0:
            result = b
            break
        for k in range(3):
            nx, ny = a + dx[k], b + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and arr[nx][ny] == 1:
                stack.append((nx, ny))
                visited[nx][ny] = 1


for _ in range(1, 11):
    TC = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    stack = []
    result = ''
    for i in range(100):
        if arr[99][i] == 2:
            start_y = i
    print('#{}'.format(TC),end=' ')
    dfs(99, start_y)
    print(result)
