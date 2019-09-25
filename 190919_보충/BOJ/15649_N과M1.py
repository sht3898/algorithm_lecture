import sys; sys.stdin = open('15649_input.txt', 'r')

N, M = map(int, input().split())
check = [0] * N
arr = []


def perm(k):
    if k == M:
        print(*arr)
        return
    for i in range(N):
        if not check[i]:
            check[i] = 1
            arr.append(i+1)
            perm(k + 1)
            arr.pop()
            check[i] = 0


perm(0)
