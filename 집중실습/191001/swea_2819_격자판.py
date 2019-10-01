import sys; sys.stdin = open('2819_input.txt', 'r')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y, k, r):
    if k == 7:
        result.add(r)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            solve(nx, ny, k+1, r + str(arr[nx][ny]))


for TC in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()      # set 사용하는게 시간이 더 빨라짐
    for i in range(4):
        for j in range(4):
            solve(i, j, 1, str(arr[i][j]))
    print('#{0} {1}'.format(TC, len(result)))
