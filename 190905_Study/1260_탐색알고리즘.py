import sys; sys.stdin = open('1260_input.txt', 'r')


def dfs(v):
    visited_dfs[v] = 1
    result_dfs.append(v)
    for e in arr[v]:
        if not visited_dfs[e]:
            dfs(e)


def bfs(v):
    visited_bfs[v] = 1
    stack_bfs.append(v)
    while stack_bfs:
        temp = stack_bfs.pop(0)
        result_bfs.append(temp)
        for e in arr[temp]:
            if not visited_bfs[e]:
                visited_bfs[e] = 1
                stack_bfs.append(e)


N, M, V = map(int, input().split())
arr = [[] * (N + 1) for _ in range(N+1)]
visited_dfs = [0] * (N + 1)
result_dfs = []
visited_bfs = [0] * (N + 1)
result_bfs = []
stack_bfs = []
for i in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

for j in range(len(arr)):
    arr[j] = sorted(arr[j])

dfs(V)
print(*result_dfs)

bfs(V)
print(*result_bfs)
