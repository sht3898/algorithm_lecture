import sys; sys.stdin = open('문제3.txt', 'r')

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]


def dfs(x, y):
    visit[x][y] = 1
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny]:
            dfs(nx, ny)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and arr[i][j]:
                count += 1
                dfs(i, j)

    print('#{} {}'.format(tc, count))