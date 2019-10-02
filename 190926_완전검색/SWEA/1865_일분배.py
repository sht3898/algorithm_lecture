import sys; sys.stdin = open('1865_input.txt', 'r')


def solve(k, result):
    global ans
    if k == N:
        ans = max(ans, result)
        return
    if ans > result:
        return
    for i in range(N):
        stat = (arr[k][i]) * 0.01  # if stat == 0: return 으로 생략하면 뒤의 것을 확인 못함
        if visit[i] or stat == 0 or result * stat < ans:
            continue
        visit[i] = 1
        result *= stat
        solve(k + 1, result)
        result /= stat
        visit[i] = 0
        # if not visit[i] and stat != 0 and result * stat >= ans:
        #     visit[i] = 1
        #     result *= stat
        #     solve(k+1, result)
        #     result /= stat
        #     visit[i] = 0


for TC in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    ans = -0xffffff
    solve(0, 1)
    print('#{} {:0.6f}'.format(TC, ans*100))
