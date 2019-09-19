import sys; sys.stdin = open('2606_input.txt', 'r')


def dfs(v):
    global cnt
    visit[v] = 1
    for w in arr[v]:
        if not visit[w]:
            dfs(w)


N = int(input())
M = int(input())
arr = [[]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
dfs(1)
print(visit.count(1)-1)