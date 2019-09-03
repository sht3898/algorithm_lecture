import sys; sys.stdin = open('4881_input.txt', 'r')


def perm(k, n, used, cursum):
    global MIN
    if cursum >= MIN:
        return

    if k == n:
        MIN = min(MIN, cursum)
        return

    for i in range(n):
        if used & (1 << i):
            continue

        perm(k + 1, n, used | (1 << i), cursum + arr[k][i])


T = int(input())
for TC in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    MIN = 0xffffff
    perm(0, N, 0, 0)
    print('#{} {}'.format(TC, MIN))
