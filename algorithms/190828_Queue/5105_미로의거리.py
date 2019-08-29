import sys; sys.stdin = open('5105_input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    queue = []
    visit = [0] * (n + 1)
    for i in range(n):
        if maze[n][i] == 2:
            visit[n][i] = True
            queue.append(maze[n][i])
    while queue:
        v = queue.pop(0)
