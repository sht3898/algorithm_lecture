import sys; sys.stdin = open('5120_input.txt', 'r')

T = int(input())

for TC in range(1, T+1):
    N, M, K = map(int, input().split())     # N: 숫자 개수, M: 지정 위치로부터의 칸, K:반복횟수
    arr = list(map(int, input().split()))
    idx = 0
    for _ in range(1, K+1):
        idx += M
        if idx < N:
            arr.insert(idx, arr[idx-1] + arr[idx])
        else:
            if idx % N:
                idx = idx % N
                arr.insert(idx, arr[idx - 1] + arr[idx])
            else:
                arr.insert(idx, arr[- 1] + arr[0])
        N += 1
    print('#{} '.format(TC), end='')
    print(*arr[-1:-11:-1])
    # print(' '.join(map(str, arr[-1:-11:-1])))
