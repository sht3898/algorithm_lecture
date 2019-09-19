import sys; sys.stdin = open('1405_input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def robot(step, x, y):
    if visited[x][y]:
        return 0
    if step >= N:
        return 1
    potential = 0
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        potential += (poten[i] / 100.0) * robot(step+1, nx, ny)
    visited[x][y] = 0
    return potential


poten = [''] * 4
N, poten[0], poten[1], poten[2], poten[3] = map(int, input().split())
visited = [[0] * 30 for _ in range(30)]
print('{}'.format(robot(0, 15, 15)))
