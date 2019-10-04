import sys; sys.stdin = open('17471_input.txt', 'r')


def DFS(v, group, visit):
    visit[v] = True
    for w in G[v]:
        if w in group and not visit[w]:
            DFS(w, group, visit)


N = int(input())    # 구역의 수
arr = [0] + list(map(int, input().split())) # 각 구역의 인구수
G = [[]]        # 인접 리스트
for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.pop(0)
    G.append(tmp)

ans = 1000 # 10 * 100
for sett in range(2, 1 << (N + 1)):
    A, B = [], []
    Asum, Bsum = 0, 0   # 인구의 합
    for i in range(1, N + 1):
        if sett & (1 << i):
            A.append(i)
            Asum += arr[i]
        else:
            B.append(i)
            Bsum += arr[i]
    if len(A) == 0 or len(B) == 0: continue
    if abs(Asum - Bsum) >= ans: continue

    visit = [False] * (N + 1)
    DFS(A[0], A, visit)
    if len(A) != visit.count(True): continue

    visit = [False] * (N + 1)
    DFS(B[0], B, visit)
    if len(B) != visit.count(True): continue

    ans = min(ans, abs(Asum - Bsum))

if ans == 1000: ans = -1

print(ans)
