import sys; sys.stdin = open('15650_input.txt', 'r')

N, M = map(int, input().split())
arr = []


def solve(k, s):
    if k == M:
        print(*arr)
        return
    for i in range(s, N):
        arr.append(i+1)
        solve(k+1, i)
        arr.pop()


solve(0, 0)
