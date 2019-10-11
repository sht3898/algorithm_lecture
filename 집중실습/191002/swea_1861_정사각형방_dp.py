import sys; sys.stdin = open('1861_input.txt', 'r')


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for TC in range(1, int(input()) + 1):
    N = int(input())
    D = [1] * (N * N + 1)
    num = [0] * (N * N + 1)
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            num[arr[i][j]] = (i, j)

    for i in range(2, N * N + 1):
        for j in range(4):
            nx, ny = num[i][0] + dx[j], num[i][1] + dy[j]
            if 0 <= nx < N and 0 <= ny < N and i - 1 == arr[nx][ny]:
                D[i] = D[i - 1] + 1
                break
    val, maxL = N * N, 0
    for i in range(1, N * N + 1):
        if D[i] > maxL:
            val, maxL = i, D[i]

    print('#{} {} {}'.format(TC, val - (maxL - 1), maxL))
