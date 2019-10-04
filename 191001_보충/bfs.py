# 너비 우선 탐색
# 필요한 것들
# 1. 그래프 2. 큐 3. 방문 정보
# 정점, 간선의 수
# 정점을 구분하기 위한 식별값 --> 정점 수가 V 개라면 1 ~ V 번까지 번호를 부여
# 따라서, 하나의 간선은 (정점번호, 정점번호)
import collections

V, E = map(int, input().split())    # V: 정점수, E: 간선수
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # 무향 그래프

Q = collections.deque()
visit = [False] * (V + 1)

# 시작점을 먼저 방문하고 큐에 삽입
Q.append(1); visit[1] = True; print(1, end=' ')
# 빈 큐가 아닐동안
while Q:
    v = Q.popleft()         # 큐에서 정점(v)을 하나 꺼내온다.
    for w in G[v]:          # v의 인접 정점(w)을 하나씩 찾아서
        if not visit[w]:    # w를 아직 방문하지 않았다면 방문하고,
            Q.append(w); visit[w] = True; print(w, end=' ')
                            # w를 큐에 삽입


# -------------------------------------------------------------------------
# 최단 경로
# BFS 로 탐색하면, 시작점에서 임의의 정점을 처음 방문할 때, 최단 경로를 확정할 수 있다.
# P, D = [], []     P = 최단 경로 트리를 저장(부모 정보를 저장)
#                   D = 시작점에서 각 정점까지 최단 거리를 저장

'''
import collections
V, E = map(int, input().split())    # V: 정점수, E: 간선수
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # 무향 그래프

Q = collections.deque()
visit = [False] * (V + 1)
P, D = [0] * (V + 1), [0] * (V + 1)
Q.append(1); visit[1] = True
result = []

while Q:
    v = Q.popleft()
    for w in G[v]:
        if not visit[w]:
            Q.append(w); visit[w] = True
            D[w] = D[v] + 1 # 시작점에서 바로 전에 방문한 정점까지 최단거리 + 1
            P[w] = v    # 바로 전에 방문한 정점을 저장

print(D[1:])
print(P[1:])
'''

# -------------------------------------------------------------------------
'''
import collections
V, E = map(int, input().split())    # V: 정점수, E: 간선수
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # 무향 그래프

Q = collections.deque()
visit = [False] * (V + 1)
P, D = [0] * (V + 1), [0] * (V + 1)
Q.append((1, 0))
visit[1] = True

while Q:
    v, d = Q.popleft()
    if v == target:     # 도착점

    for w in G[v]:
        if not visit[w]:
            Q.append(w); visit[w] = True
            D[w] = D[v] + 1 # 시작점에서 바로 전에 방문한 정점까지 최단거리 + 1
            P[w] = v    # 바로 전에 방문한 정점을 저장

print(D[1:])
print(P[1:])
'''