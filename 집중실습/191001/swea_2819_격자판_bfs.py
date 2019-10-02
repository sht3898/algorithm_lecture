import sys; sys.stdin = open('2819_input.txt', 'r')
import collections


def BFS(sx, sy):
    global ans
    Q = collections.deque()
    Q.append((sx, sy, 1, pan[sx][sy]))

    while Q:
        x, y, l, key = Q.popleft()
        if l == 7:
            if key not in dic:
                ans += 1
                dic[key] = 1
        else:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                tx, ty = x + dx, y + dy
                if 0 <= tx < 4 and 0 <= ty < 4:
                    Q.append((tx, ty, l + 1, key + pan[tx][ty]))


T = int(input())
for TC in range(1, T + 1):
    pan = [list(input().split()) for _ in range(4)]
    dic = dict()
    ans = 0
    for i in range(4):
        for j in range(4):
            BFS(i, j)
    print('#{0} {1}'.format(TC, ans))
