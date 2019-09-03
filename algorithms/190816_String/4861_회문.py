import sys; sys.stdin = open('회문.txt', 'r')

T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    switch = 0

    for i in range(N):
        if switch:
            break
        for j in range(N-M+1):
            temp = ''
            for k in range(M):
                temp += arr[i][j+k]
            if temp == temp[::-1]:
                result = temp
                switch = 1
                break

    for j in range(N):
        if switch:
            break
        for i in range(N-M+1):
            temp = ''
            for k in range(M):
                temp += arr[i+k][j]
            if temp == temp[::-1]:
                result = temp
                break

    print('#{} '.format(TC), end='')
    print(result)