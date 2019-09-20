import sys; sys.stdin = open('15650_input.txt', 'r')

N, M = map(int, input().split())
arr = []
check = [0] * N


def solve(k, n):
    if k == M:
        print(*arr)
        return
    for i in range(n):
        arr.append(i+1)
        check[i] = 1
        solve(k+1, n)
        check[i] = 0
        arr.pop()


solve(0, N)
