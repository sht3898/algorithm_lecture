import sys; sys.stdin = open('2210_input.txt', 'r')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(k, x, y):
    if k == 6:
        return
    for i in range(4):
        pass


arr = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
cnt = 0
numsum = 0