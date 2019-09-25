import sys; sys.stdin = open('1697_input.txt' ,'r')
from collections import deque


def bfs(v):
    q = deque()
    visited = [0] * 100001
    q.append(v)
    time = 0
    state = 0
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            if not visited[x]:
                visited[x] = 1
                if x == K:
                    state = 1
                    break
                if x - 1 >= 0:
                    q.append(x-1)
                if x + 1 <= 100000:
                    q.append(x+1)
                if 0 <= 2 * x <= 100000:
                    q.append(2*x)
        if state:
            print(time)
            break
        time += 1
        

N, K = map(int, input().split())
bfs(N)
