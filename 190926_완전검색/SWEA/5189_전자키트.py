import sys; sys.stdin = open('5189_input.txt', 'r')


def path(k):
    if k == N-1:
        paths.append([0]+arr+[0])
        return
    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            arr.append(i)
            path(k+1)
            arr.pop()
            visited[i] = 0


def solve(lst):
    total = 0
    while len(lst) >= 2:
        x, y = lst[0], lst[1]
        total += numbers[x][y]
        lst.pop(0)
    return result.append(total)


for TC in range(1, int(input())+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N + 1)
    result = []
    arr = []
    paths = []
    path(0)
    for i in paths:
        solve(i)
    print('#{}'.format(TC), end=' ')
    print(min(result))
