import sys; sys.stdin = open('IM.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    rectangle = [[0] * n for _ in range(m)]
    colors = [0] * 11
    for _ in range(k):
        arr = list(map(int, input().split()))
        a, b, color = arr[:2], arr[2:4], arr[-1]
        x1, x2, y1, y2 = min(a[0], b[0]), max(a[0], b[0]), min(a[1], b[1]), max(a[1], b[1])
        high = 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if high <= rectangle[i][j]:
                    high = rectangle[i][j]

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if high <= color:
                    rectangle[i][j] = color
                else:
                    break

    for i in range(m):
        for j in range(11):
            colors[j] += rectangle[i].count(j)
    print('#{} {}'.format(tc, max(colors)))
