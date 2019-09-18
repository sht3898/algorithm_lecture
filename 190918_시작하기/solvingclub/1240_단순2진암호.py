import sys; sys.stdin = open('1240_input.txt', 'r')

NUM = {'3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4, '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9}


def password(arr):
    n = len(arr)
    prev = arr[0]
    cnt = 1
    result = ''
    for i in range(1, n):
        if arr[i] == prev:
            cnt += 1
        else:
            result += str(cnt)
            cnt = 1
        prev = arr[i]
    result += str(cnt)
    return result


T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    numbers = []
    final = []
    switch = 0
    for i in range(N-1, -1, -1):
        if switch:
            break
        for j in range(M-1, -1, -1):
            if arr[i][j] != 0:
                start_x, start_y = i, j-55
                switch = 1
                break
    for x in range(0, 50, 7):
        numbers.append(arr[start_x][start_y+x:start_y+x+7])
    for i in numbers:
        final.append(NUM[password(i)])
    odd = (final[0] + final[2] + final[4] + final[6]) * 3
    even = final[1] + final[3] + final[5]
    if (odd + even + final[-1]) % 10:
        print('#{} 0'.format(TC))
    else:
        print('#{} {}'.format(TC, sum(final)))
