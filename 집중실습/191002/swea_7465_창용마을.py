import sys; sys.stdin = open('7465_input.txt', 'r')


def solve(v):
    visit[v] = 1
    for w in people[v]:
        if not visit[w]:
            solve(w)
    return


for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    people = [[] * (N + 1) for _ in range(N + 1)]
    visit = [0] * (N + 1)
    cnt = 0
    for i in arr:
        people[i[0]].append(i[1])
        people[i[1]].append(i[0])
    for i in range(1, N + 1):
        if not visit[i]:
            solve(i)
            cnt += 1
    print('#{} {}'.format(TC, cnt))
