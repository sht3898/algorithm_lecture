import sys; sys.stdin = open('1405_input.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    visited[x][y] = 1


N, e, w, s, n = map(int, input().split())
potential = [float(e)/100, float(w)/100, float(s)/100, float(n)/100]
arr = [[0] * 30 for _ in range(30)]
visited = [[0] * 30 for _ in range(30)]
start_x, start_y = 15, 15
