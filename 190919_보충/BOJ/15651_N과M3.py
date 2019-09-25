import sys; sys.stdin = open('15650_input.txt', 'r')

N, M = map(int, input().split())
arr = []
check = [0] * N


def solve(k):
    if k == M:
        print(*arr)
        return
    for i in range(N):
        arr.append(i+1)
        check[i] = 1
        solve(k+1)
        check[i] = 0
        arr.pop()


solve(0)
