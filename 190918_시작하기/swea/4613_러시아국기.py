import sys; sys.stdin = open('4613_input.txt', 'r')
import pprint
T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(M):
        if arr[0][i] != 'W':
            arr[0][i] = 'W'
            cnt += 1
        if arr[-1][i] != 'R':
            arr[-1][i] = 'R'
            cnt += 1

    for i in range(1, N):
        if arr[i-1][0] == 'W':
            if arr[i].count('W') >= arr[i].count('B') + arr[i].count('R'):
                for j in range(M):
                    if arr[i][j] != 'W':
                        arr[i][j] = 'W'
                        cnt += 1
            else:
                for j in range(M):
                    if arr[i][j] != 'B':
                        arr[i][j] = 'B'
                        cnt += 1
        elif arr[i-1][0] == 'B':
            if arr[i].count('B') >= arr[i].count('W') + arr[i].count('R'):
                for j in range(M):
                    if arr[i][j] != 'B':
                        arr[i][j] = 'B'
                        cnt += 1
            else:
                for j in range(M):
                    if arr[i][j] != 'R':
                        arr[i][j] = 'R'
                        cnt += 1
        else:
            for j in range(M):
                if arr[i][j] != 'R':
                    arr[i][j] = 'R'
                    cnt += 1

    pprint.pprint(arr)
    print(cnt)
