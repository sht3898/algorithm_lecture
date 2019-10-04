import sys; sys.stdin = open('17471_input.txt', 'r')


def connect(lst):
    for i in lst:
        if i in dist[i]:
            return True
    return False


def solve(k, n):
    global temp, ans
    if k == n:
        result2 = [x for x in numbers if x not in result]
        if connect(result) and connect(result2):
            for i in result:
                temp += i
            ans = min(abs(temp-pop_sum), ans)
        return

    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = 1
            result.append(i)
            solve(k+1, n)
            result.pop()
            visit[i] = 0


N = int(input())
population = [0] + list(map(int, input().split()))
pop_sum = sum(population)
numbers = [i for i in range(1, N+1)]
arr = [[]] + [list(map(int, input().split())) for _ in range(N)]
dist = [[] * (N + 1) for _ in range(N + 1)]
visit = [0] * (N + 1)
result = []
ans = 0
for i in range(1, N+1):
    for j in range(1, arr[i][0]+1):
        dist[i].append(arr[i][j])
for num in range(1, N):
    temp = 0
    solve(0, num)
print(ans)
