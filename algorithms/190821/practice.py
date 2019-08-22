def dfs(v):
    visit[v] = 1
    path.append(v)

    for w in graph[v]:
        if not visit[w]:
            dfs(w)


t = int(input())


for tc in range(1, t + 1):
    v, e = map(int, input().split())
    node = []
    graph = [[] for _ in range(v+1)]
    visit = [0] * (v + 1)
    path = []
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
    s, g = map(int, input().split())

    dfs(s)
    print('#{} {}'.format(tc, visit[g]))
