import sys; sys.stdin = open('1861_input.txt', 'r')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y, cnt, sx, sy):
    global MAX, result

    if MAX <= cnt:
        if MAX == cnt:
            result = min(result, arr[sx][sy])
        else:
            result = arr[sx][sy]
        MAX = cnt
    if cnt == N**2:
        return
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] - arr[x][y] == 1:
                solve(nx, ny, cnt+1, sx, sy)


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    MAX = 0
    result = 0xfffff
    for i in range(N):
        for j in range(N):
            solve(i, j, 1, i, j)
    print('#{} {} {}'.format(TC, result, MAX))
