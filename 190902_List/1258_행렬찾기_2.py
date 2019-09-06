import sys; sys.stdin = open('1258_input.txt', 'r')


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue

            r, c = i, 0  # r: 행, c: 열
            while r < N and arr[r][j]:
                c = j
                while c < N and arr[r][c]:
                    arr[r][c] = 0
                    c += 1
                r += 1

            ans.append((r - i, c - j))

    ans.sort(key=lambda a: (a[0] * a[1], a[0]))
    print('#{}'.format(TC), end='')
    for i in ans:
        print(' {} {}'.format(i[0], i[1]),end='')
    print()