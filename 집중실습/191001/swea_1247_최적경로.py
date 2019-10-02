import sys; sys.stdin = open('1247_input.txt', 'r')


def solve(location, k):
    global result, ans
    if result > ans:
        return
    if k == N:
        result += abs(location[0]-home[0]) + abs(location[1]-home[1])
        ans = min(result, ans)
        result -= abs(location[0] - home[0]) + abs(location[1] - home[1])
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            result += (abs(location[0]-customers[i][0]) + abs(location[1]-customers[i][1]))
            solve(customers[i], k+1)
            result -= (abs(location[0]-customers[i][0]) + abs(location[1]-customers[i][1]))
            visit[i] = 0


for TC in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    visit = [0] * N
    company = arr[:2]
    home = arr[2:4]
    result = 0
    ans = 0xfffffff
    customers = []
    for i in range(N):
        customers.append([arr[2*i+4], arr[2*i+5]])
    solve(company, 0)
    print('#{} {}'.format(TC, ans))
