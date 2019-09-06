import sys; sys.stdin = open('5099_input.txt', 'r')

T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())    # N: 화덕의 크기, M: 피자의 크기
    arr = list(map(int, input().split()))
    fire = [[arr[i], i + 1] for i in range(N)]
    i = 0
    while len(fire) != 1:
        fire[0][0] //= 2

        if fire[0][0] == 0:
            if N < M - i:
                fire.pop(0)
                fire.append([arr[N+i], N+i+1])
                i += 1
            elif N >= M - i:
                fire.pop(0)
        else:   #
            fire.append(fire.pop(0))

    print('#{}'.format(TC), end=' ')
    print(fire[0][1])
