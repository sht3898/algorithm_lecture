# 부분집합 활용


import sys; sys.stdin = open('3752_input.txt', 'r')
# ---------------------------------------------------------------------------------------
# dfs


def backtrack(k, s):    # k: 트리의 높이, 문항번호, s: 지금까지 점수의 합
    global cnt
    if visited[k][s]: return    # 높이 k에서 s가 나올때 있으면 생략
    visited[k][s] = 1
    if k == N:      # 높이가 끝까지 갔으면 cnt 증가
        cnt += 1
    else:
        backtrack(k+1, s)           # k번 문제를 틀림
        backtrack(k+1, s + arr[k])  # k번 문제를 맞음


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [[0] * (N * 100 + 1) for _ in range(N + 1)]
    cnt = 0
    backtrack(0, 0)
    print('#{} {}'.format(TC, cnt))

# ---------------------------------------------------------------------------------------
# bfs => 제대로 안나옴

for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [[0] * (N * 100 + 1) for _ in range(N + 1)]
    cnt = 0

    q = []
    q.append(0)
    for k in range(len(arr)):
        for i in range(len(q)):
            t = q[i] + arr[k]
            if visited[k][t] == 0:
                q.append(t)
                visited[k][t] = 1

    print('#{} {}'.format(TC, len(q)))

# ---------------------------------------------------------------------------------------
# 집합
for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    A = set()
    A.add(0)
    for s in arr:
        B = set()
        for a in A:
            B.add(s + a)
        A = A | B
    print('#{} {}'.format(TC, len(A)))
