import sys; sys.stdin = open('2667_input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global cnt
    visited[x][y] = 1
    if not arr[x][y]:
        return
    cnt += 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny]:
            dfs(nx, ny)


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt = 0
            dfs(i, j)
            if cnt:
                result.append(cnt)
print(len(result))
result = sorted(result)
for l in result:
    print(l)
