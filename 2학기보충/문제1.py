import sys; sys.stdin = open('문제1.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        count = 0
        x1, y1, x2, y2 = map(int, input().split())
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] += 1
    for i in arr:
        for j in i:
            if j != 0:
                count += 1
    print('#{} {}'.format(tc, count))