import sys; sys.stdin = open('1231_input.txt', 'r')


def solve(v):
    global result

    if len(arr[v]) >= 3:
        solve(int(arr[v][2]))
    result += arr[v][1]
    if len(arr[v]) == 4:
        solve(int(arr[v][3]))


for TC in range(1, 11):
    N = int(input())
    arr = [[]]
    result = ''
    for i in range(N):
        arr.append(list(input().split()))
    solve(1)
    print('#{} {}'.format(TC, result))
