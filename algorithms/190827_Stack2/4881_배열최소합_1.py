import sys; sys.stdin = open('4881_input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = []
    for j in range(n):
        visit = [[0] * n for _ in range(n)]
        sum = 0
        for i in range(n):
            if not visit[i][j]:
                sum += arr[i][j]
                for k in range(n):
                    visit[i][k] = 1
                    visit[k][j] = 1
        result.append(sum)
        print(result)
