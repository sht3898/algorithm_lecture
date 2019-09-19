import sys; sys.stdin = open('10026_input.txt', 'r')
# def dfs(x, y, red):
#     visited[x][y] = 1
#     for k in range(4):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#             if red == 1 and arr[i][j] == 'B' and (arr[nx][ny] == 'R' or arr[nx][ny] == 'G'):
#                 continue
#             if red == 1 and arr[i][j] != 'B' and arr[nx][ny] == 'B':
#                 continue
#             if red == 0 and arr[nx][ny] != arr[i][j]:
#                 continue
#             dfs(nx, ny, red)


# def dfs(i, j, red):
#     stack.append((i, j))
#     visited[i][j] = 1
#     while stack:
#         x, y = stack.pop()
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                 if red == 1 and arr[i][j] == 'B' and (arr[nx][ny] == 'R' or arr[nx][ny] == 'G'):
#                     continue
#                 if red == 1 and arr[i][j] != 'B' and arr[nx][ny] == 'B':
#                     continue
#                 if red == 0 and arr[nx][ny] != arr[i][j]:
#                     continue
#                 stack.append((nx, ny))
#                 visited[nx][ny] = 1
from collections import deque


def bfs(i, j, red):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if red == 1 and arr[i][j] == 'B' and (arr[nx][ny] == 'R' or arr[nx][ny] == 'G'):
                    continue
                if red == 1 and arr[i][j] != 'B' and arr[nx][ny] == 'B':
                    continue
                if red == 0 and arr[nx][ny] != arr[i][j]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())

arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
stack = []
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, 0)
            cnt += 1
print(cnt, end=' ')
cnt = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, 1)
            cnt += 1
print(cnt)
