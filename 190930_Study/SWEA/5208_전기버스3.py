import sys; sys.stdin = open('5208_input.txt', 'r')


def solve(idx, stop, cnt):
    global result
    if cnt >= result:
        return
    if idx + stop >= N:
        result = cnt
        return
    for j in range(idx + 1, idx + stop + 1):
        solve(j, arr[j], cnt+1)


for TC in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N, station = arr[0], arr[1:]
    result = N
    solve(1, station[0], 0)
    print('#{} {}'.format(TC, result))
