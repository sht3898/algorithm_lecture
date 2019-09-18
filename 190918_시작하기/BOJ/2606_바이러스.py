import sys; sys.stdin = open('2606_input.txt', 'r')

N = int(input())
M = int(input())
arr = [[]*(N+1) for _ in range(N+1)]
q = []
visit = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

visit[1] = 1
q.append(1)
while q:
    temp = q.pop(0)
    for w in arr[temp]:
        visit
