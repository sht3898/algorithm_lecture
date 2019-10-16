import sys; sys.stdin = open('graph.txt', 'r')
from collections import deque



def BFS(s):
    D = [0xffffff] * (V + 1)
    visit = [False] * (V + 1)
    D[s] = 0
    cnt = V

    while cnt:

        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] += D[u] + w
        cnt -= 1


V, E = map(int, input().split())        # 정점수, 간선수
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

pi = [0] * (V + 1)
key = [0xffffff] * (V + 1)
