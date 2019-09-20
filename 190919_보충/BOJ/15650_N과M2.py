import sys; sys.stdin = open('15650_input.txt', 'r')

N, M = map(int, input().split())
arr = []
check = [0] * N


def solve(k, s):
    if k == M:
        print(*sorted(arr))
        return
    for i in range(s, N):
        if not check[i]:
            check[i] = 1
            arr.append(i+1)
            solve(k+1, i)
            arr.pop()
            check[i] = 0


solve(0, 0)
