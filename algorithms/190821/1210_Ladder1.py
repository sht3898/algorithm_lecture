import sys; sys.stdin = open('1210_input.txt', 'r')

dy = [-1, 0, 0]
dx = [0, -1, 1]

for _ in range(10):
    t = input()
    stack = []
    visit = [[False]*100 for _ in range(100)]
    ladders = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladders[99][i] == 2:
            stack.append((99, i))
            visit[99][i] = True

    while stack:
        y, x = stack.pop()
        if y == 0:
            result = x
            break
        for i in range(3):
            d_y, d_x = y + dy[i], x + dx[i]
            if 0 <= d_y < 100 and 0 <= d_x < 100:
                if not visit[d_y][d_x] and ladders[d_y][d_x]:
                    stack.append((d_y, d_x))
                    visit[d_y][d_x] = True

    print('#{} {}'.format(t, result))