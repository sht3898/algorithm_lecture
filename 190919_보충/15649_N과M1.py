import sys; sys.stdin = open('15649_input.txt', 'r')

# N, M = map(int, input().split())
# visit = [0] * N
# order = []
#
#
# def perm(k, n):
#     if k == n:
#         print(*order)
#         return
#     for i in range(N):
#         if visit[i]: continue
#         visit[i] = 1
#         order.append(i)
#         perm(k+1, n)
#         visit[i] = 0
#         order.pop()
#         perm(k+1, n)
#
#
# perm(0, M)
n, m = map(int, input().split())
check = [False]*n
a = []

def solve(cnt):
    if cnt == m:
        print(" ".join(map(str, a)))
        return
    for i in range(n):
        if not check[i]:
            check[i] = True
            a.append(i+1)
            solve(cnt+1)
            a.pop()
            check[i] = False

solve(0)