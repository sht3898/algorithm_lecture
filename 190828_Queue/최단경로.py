from collections import deque
V, E = map(int, input().split())
G = [[] for _ in range(V +1)]
D = [0] * (V + 1) # 최단 거리를 저장
P = [0] * (V + 1) # 최단경로 트리


def bfs(s):
    Q = deque()
    visit = [False] * (V + 1) # 1~V 까지
    visit[s] = True;
    Q.append(s)
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)