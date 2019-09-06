import sys; sys.stdin = open('1238_input.txt', 'r')


def bfs(start):
    queue = []
    visit[start] = 1
    queue.append(start)
    result = []
    temp = []
    while queue:
        for i in range(len(queue)):
            q = queue.pop(0)
            for w in G[q]:
                if not visit[w]:
                    visit[w] = 1
                    queue.append(w)
                    result.append(w)
        if result:
            temp = result.copy()
            result = []
    return temp


for t in range(1, 11):
    L, start = map(int, input().split())
    tel = list(map(int, input().split()))
    N = max(tel)
    G = [[] for _ in range(N+1)]
    visit = [0] * (N+1)
    for i in range(L // 2):
        G[tel[2 * i]].append(tel[2 * i + 1])

    anw = bfs(start)
    print('#{} {}'.format(t, max(anw)))