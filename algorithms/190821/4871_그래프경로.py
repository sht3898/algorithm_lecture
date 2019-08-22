import sys; sys.stdin = open('4871_input.txt', 'r')

# 모든 경로를 찾은 후, 경로에 s, g가 들어있나 확인


def dfs(v):
    stack = []
    visit[v] = True
    path.append(v)
    stack.append(v)
    while stack:
        for w in graph[v]:
            if not visit[w]:
                visit[w] = True
                path.append(w)
                stack.append(v)
                v = w
                break
        else:
            v = stack.pop()


t = int(input())


for tc in range(1, t + 1):
    v, e = map(int, input().split())
    node = []
    graph = [[] for _ in range(v+1)]
    visit = [False] * (v + 1)
    path = []
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
    s, g = map(int, input().split())

    dfs(s)
    if g in path:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))