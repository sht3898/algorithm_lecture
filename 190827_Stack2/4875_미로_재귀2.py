import sys; sys.stdin = open('4875_input.txt', 'r')

sx = sy = ex = ey = 0


def DFS(x, y):
    if maze[x][y] == '3': return True

    maze[x][y] = '1'

    for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx, ty = x + dx, y + dy
        if tx < 0 or tx == n or ty < 0 or ty == n or maze[tx][ty] == '1': continue
        if DFS(tx, ty):
            maze[x][y] = 0
            return True

        maze[x][y] = '0'
        return False


t = int(input())
for tc in range(1, t+1):
    n = int(input())

    maze = []
    visit = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        maze.append(input())
        for j in range(n):
            if maze[i][j] == '2':
                sx, sy = i, j
            if maze[i][j] == '3':
                ex, ey = i, j
    DFS(sx, sy)
    print('#{} {}'.format(tc, visit[ex][ey]))