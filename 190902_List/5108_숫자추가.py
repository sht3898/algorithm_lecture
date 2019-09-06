import sys; sys.stdin = open('5108_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        idx, num = map(int, input().split())
        tmp = arr[idx:]
        arr[idx] = num
        arr = arr[:idx+1] + tmp
    print('#{} {}'.format(tc, arr[L]))