import sys; sys.stdin = open('1244_input.txt', 'r')


def find(k):
    global ans
    result = int(''.join(arr))
    if k == cnt:
        ans = max(ans, result)
        return
    if visited[result]:
        return
    visited[result] = 1
    for i in range(N):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            find(k+1)
            arr[i], arr[j] = arr[j], arr[i]


for TC in range(1, int(input()) + 1):
    arr, cnt = input().split()
    arr = list(arr)
    N, cnt = len(arr), int(cnt)
    ans = 0
    visited = [0 for _ in range(999999+1)]
    find(0)
    print('#{} {}'.format(TC, ans))
