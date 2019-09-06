import sys; sys.stdin = open('DFS_input.txt', 'r')


def DFS(v):  # v = 현재 방문하는 정점
    # 시작점을 방문하고, 스택에 push

    visit[v] = True
    print(v,  end=' ')

    for w in G[v]:
        if not visit[w]:
            DFS(w)


V, E = map(int, input().split())    # 정점수, 간선수
G = [[] for _ in range(V + 1)]      # 1 ~ V 까지
visit = [False] * (V + 1)           # 방문정보

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # 무향 그래프니까

DFS(1)