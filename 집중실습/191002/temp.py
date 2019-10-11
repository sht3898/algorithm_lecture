import sys; sys.stdin = open('1861_input.txt', 'r')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y, cnt):
    global MAX, final
    MAX = max(MAX, cnt)
    flag = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] - arr[x][y] == 1:
            solve(nx, ny, cnt+1)
            flag = 1
    if flag == 0:
        return


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    MAX = 0
    result = 0
    for i in range(N):
        for j in range(N):
            solve(i, j, 0)

    print('#{} {} {}'.format(TC, final, result))
