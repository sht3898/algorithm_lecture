import sys; sys.stdin = open('문제3.txt', 'r')
import pprint

t = int(input())

def dfs(a, b):
    x, y = i[a], i[b]
    count = 0
    if not visit[x][y]:
        visit[x][y] = True
    for direction in range(3):
        d_x, d_y = x + dx[direction], y + dy[direction]
        if 0 <= d_x < n and 0 <= d_y < n and not visit[d_x][d_y] and island[d_x][d_y] != 0:
            x, y = d_x, d_y
            dfs(x, y)
        elif 0 <= d_x < n and 0 <= d_y < n and not visit[d_x][d_y] and island[d_x][d_y] != 0:
            count += 1
    return count


dx = [1,1,0]
dy = [0,1,1]

for tc in range(1, t+1):
    n = int(input())
    visit = [[False]*n for _ in range(n)]
    island = [list(map(int, input().split())) for _ in range(n)]
    stack = []
    count = 0

    for x in range(n):
        for y in range(n):
            if island[x][y] != 0:
                stack.append([x, y])
    for i in stack:
        x, y = i[0], i[1]
        for j in range(3):
            d_x, d_y = x + dx[j], y + dy[j]
            if d_x