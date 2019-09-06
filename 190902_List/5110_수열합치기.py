import sys; sys.stdin = open('5110_input.txt', 'r')


T = int(input())

for TC in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(M):
        numbers = list(map(int, input().split()))
        for i in range(len(arr)):
            if arr[i] > numbers[0]:
                arr = arr[:i] + numbers + arr[i:]
                break
        else:
            arr += numbers

    print('#{} '.format(TC), end='')
    print(*arr[-1:-11:-1])
