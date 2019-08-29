import sys; sys.stdin = open('4881_input.txt', 'r')


def perm(k, n, used, cursum):
    global MIN
    if cursum >= MIN: return

    if k == n:
        MIN = min(MIN, cursum)
        return

    for i in range(n):
        if used & (1 << i): continue

        perm(k+1, n, used | (1<<i), cursum + arr[k][i])


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
