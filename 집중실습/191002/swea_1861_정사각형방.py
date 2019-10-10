import sys; sys.stdin = open('1861_input.txt', 'r')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y):
    global cnt, ans, final
    if ans > cnt:
        return
    if ans < cnt:
        ans = cnt
        final = arr[x][y]
    visit[x][y] = 1
    cnt += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and arr[nx][ny] - arr[x][y] == 1:
            solve(nx, ny)


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    ans = 0
    final = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            solve(i, j)
    print('#{} {} {}'.format(TC, final, ans))
