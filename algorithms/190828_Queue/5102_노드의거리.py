import sys; sys.stdin = open('5102_input.txt', 'r')


def bfs(s, g):
    global result
    q.append(s)
    visited[s] = 1
    while q:
        temp = q.pop(0)
        for w in arr[temp]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1
                dist[w] = dist[temp] + 1
                if w == g:
                    result = dist[w]
                    return


T = int(input())

for TC in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] * (V + 1) for _ in range(V + 1)]
    dist = [0] * (V + 1)
    visited = [0] * (V + 1)
    q = []
    result = 0
    for _ in range(E):
        start, end = map(int, input().split())
        arr[start].append(end)
        arr[end].append(start)
    S, G = map(int, input().split())
    bfs(S, G)
    print('#{} {}'.format(TC, result))