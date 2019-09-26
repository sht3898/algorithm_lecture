import sys; sys.stdin = open('5188_input.txt', 'r')

dx = [1, 0]
dy = [0, 1]


def check(x, y, k):
    global total, result
    if k == 2 * N - 2:
        result = min(result, total)
        return
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            total += arr[nx][ny]
            if result >= total:
                check(nx, ny, k + 1)
            total -= arr[nx][ny]
            visited[nx][ny] = 0


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    total = arr[0][0]
    result = 0xffffff
    check(0, 0, 0)
    print('#{}'.format(TC), end=' ')
    print(result)
