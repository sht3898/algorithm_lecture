import sys; sys.stdin = open('1697_input.txt', 'r')

# dfs 로 풀면 time over

def bfs(v):
    visit = [0] * 100001
    q = [v]
    cnt = 0
    state = 0

    while q:
        for _ in range(len(q)):
            v = q.pop(0)
            if not visit[v]:
                visit[v] = 1
                if v == K:
                    state = 1
                    break
                if v - 1 >= 0:
                    q.append(v - 1)
                if v + 1 <= 100000:
                    q.append(v + 1)
                if v * 2 <= 100000:
                    q.append(v * 2)

        if state:
            print(cnt)
            break
        cnt += 1


N, K = map(int, input().split())
bfs(N)
