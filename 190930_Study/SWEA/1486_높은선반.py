import sys; sys.stdin = open('1486_input.txt', 'r')


def solve(result, s):
    global ans
    if result >= B:
        ans = min(ans, result)
        return
    for i in range(s, N):
        if not visit[i]:
            visit[i] = 1
            solve(result+arr[i], i)
            visit[i] = 0


for TC in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    visit = [0] * N
    ans = 0xfffff
    solve(0, 0)
    print('#{} {}'.format(TC, ans - B))
