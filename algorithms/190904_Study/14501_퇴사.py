N = int(input())
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

ans = 0


def backtrack(day, p):  # day: 결정할 일, p: 지금까지 이익
    global ans

    if day > N + 1: return
    if day == N + 1:
        ans = max(ans, p)
        return

    # 상담을 하는 경우
    backtrack(day + arr[day][0], p + arr[day][1])
    # 상담을 하지 않는 경우
    backtrack(day + 1, p)


backtrack(1, 0)
