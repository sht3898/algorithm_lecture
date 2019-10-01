import sys; sys.stdin = open('2819_input.txt', 'r')
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(x, y):
    global result
    q.append([x, y])
    while q:
        if len(result) == 7:
            if result not in ans:
                ans.append(result)
        else:
            temp = q.popleft()
            a, b = int(temp[0]), int(temp[1])
            result += str(arr[a][b])
            for i in range(4):
                nx, ny = a + dx[i], b + dy[i]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    q.append([nx, ny])


for TC in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    q = deque()
    ans = []
    for i in range(4):
        for j in range(4):
            result = ''
            solve(i, j)
    print('#{0} {1}'.format(TC, len(ans)))
