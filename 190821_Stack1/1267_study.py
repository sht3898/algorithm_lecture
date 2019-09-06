import sys; sys.stdin = open('1267_input.txt', 'r')
from collections import deque       # queue 사용


def bfs(graph):                     # bfs 그래프
    q = deque()
    for i in range(1, V+1):     # 꼭지점의 개수만큼 반복
        if degree[i] == 0:      # 꼭지점의 깊이가 0이라면 q에 저장
            q.append(i)     
    while q:        # q의 길이가 0 이상일때 반복
        temp = q.popleft()      # 현재 큐의 첫번째 원소를 pop
        result.append(temp)     # result 에 꺼낸 원소를 저장
        for w in graph[temp]:   # 꺼낸 원소의 다음 경로를 반복
            if degree[w] != 0:  # 깊이가 0이 아니라면 깊이를 1 감소시켜 다음 경로로 진출할 수 있게 만듦
                degree[w] -= 1
                if degree[w] == 0:  # 깊이가 0이라면 q에 저장하여 반복시킴
                    q.append(w)


for TC in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    result = []
    start = []
    degree = [0] * (V + 1)
    for i in range(E):
        G[arr[2 * i]].append(arr[2 * i + 1])
        degree[arr[2*i+1]] += 1     # 깊이 저장

    bfs(G)

    print('#{}'.format(TC), end=' ')
    print(*result)
