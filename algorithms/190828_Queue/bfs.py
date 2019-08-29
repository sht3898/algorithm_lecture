import sys; sys.stdin = open('input.txt', 'r')


def BFS(s): # s: 시작점
    Q = []
    visit = [False] * (V + 1)   # 1 ~ V까지
    visit[s] = True; print(s)
    Q.append(s)
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                Q.append(w)

    # 큐를 생성, 방문 표시
    # 시작점을 방문하고 큐에 삽입
    # 빈큐가 아닐 동안
        # 큐에서 하나 꺼내온다. v
        # v의 방문하지 않은 인접정점을 모두 찾아서
            # 차례로 방문하고 큐에 삽입


V, E = map(int, input().split())
G = [[] for _ in range(n)]