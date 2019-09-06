import sys; sys.stdin = open('1267_input.txt', 'r')
from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    result.append(v)
    while q:
        temp = q.popleft()
        for e in numbers[temp]:
            if degree[e] != 0:
                degree[e] -= 1
                if degree[e] == 0:
                    q.append(e)
            result.append(e)


for TC in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    numbers = [[] * (V + 1) for _ in range(V + 1)]
    result = []
    degree = [0] * (V + 1)
    for i in range(E):
        numbers[arr[2*i]].append(arr[2*i+1])
        degree[arr[2*i+1]] += 1

    for i in range(1, V+1):
        if degree[i] == 0:
            bfs(i)
            break
    print(*result)