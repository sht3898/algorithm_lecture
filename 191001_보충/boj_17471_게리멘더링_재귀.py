import sys; sys.stdin = open('17471_input.txt', 'r')


def DFS(v, group, visit):
    visit[v] = True
    ret = 1
    for w in G[v]:
        if w in group and not visit[w]:
            ret += DFS(w, group, visit)
    return ret
# k: 결정할 구여번호, A,B = 그룹 리스트, sumA =A에 속한 구역의 인구수합


def backtrack(k, A, B, sumA):
    if k == N + 1:
        global ans
        diff = abs(sumA * 2 - total)
        if len(B) == 0 or diff >= ans: return
        visit = [False] * (N + 1)
        if(DFS(A[0], A, visit) != len(A)): return
        visit = [False] * (N + 1)
        if(DFS(B[0], B, visit) != len(B)): return
        ans = diff
    else:
        A.append(k)     # k번 구역을 A에 포함
        backtrack(k + 1, A, B, sumA + arr[k])
        A.pop()
        B.append(k)     # k번 구역을 B에 포함
        backtrack(k + 1, A, B, sumA)
        B.pop()


N = int(input())
arr = [0] + list(map(int, input().split())) # 인구수
G = [[]]                                    # 인접 리스트

for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.pop(0)
    G.append(tmp)
ans = 1000

A, B = [], []
total = sum(arr)
A.append(1)
backtrack(2, A, B, arr[1])

if ans == 1000:
    ans = -1
print(ans)
