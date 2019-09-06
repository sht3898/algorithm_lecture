import sys; sys.stdin = open('2606_input.txt', 'r')


def dfs(v):
    global cnt
    visited[v] = 1
    for e in arr[v]:
        if not visited[e]:
            cnt += 1
            dfs(e)


N = int(input())
M = int(input())
arr = [[] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0
for _ in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)
dfs(1)
print(cnt)
