import sys; sys.stdin = open('3980_input.txt', 'r')


def solve(k, s):
    global result
    if k == 11:
        result = max(result, s)
        return
    for j in range(11):
        stat = S[k][j]
        if not visit[j] and stat != 0:
            visit[j] = 1
            solve(k+1, s+stat)
            visit[j] = 0


C = int(input())

for TC in range(1, C+1):
    S = [list(map(int, input().split())) for _ in range(11)]
    visit = [0] * 11
    result = -0xfffff
    solve(0, 0)
    print(result)
