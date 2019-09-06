import sys; sys.stdin = open('5105_input.txt', 'r')
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global result       # 외부 변수인 result 를 사용
    q.append((x, y))    # q에 시작 좌표를 저장
    visited[x][y] = 1   # 시작 좌표를 방문 표시
    while q:    # q에 원소가 존재하는 동안 반복
        start_x, start_y = q.popleft()      # q의 첫번째 원소를 pop 하여
        for i in range(4):      # 네 방향을 반복하며 경로가 있나 탐색
            nx, ny = start_x + dx[i], start_y + dy[i]   
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
                q.append((nx, ny))
                visited[nx][ny] = 1
                dist[nx][ny] = dist[start_x][start_y] + 1
                if arr[nx][ny] == 3:        # 새로운 좌표의 값이 3일때 원래 늘렸던 결과값을 1 줄이고 bfs 를 종료
                    result = dist[nx][ny] - 1
                    return


T = int(input())
for TC in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * (N + 1) for _ in range(N)]     # 방문 좌표 저장
    dist = [[0] * (N + 1) for _ in range(N)]    # 거리 저장
    result = 0      # 결과 저장
    q = deque()     # bfs 에서 좌표를 저장할 스택
    for i in range(N):      # 시작 좌표 찾기
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j
                break
    bfs(x, y)
    print('#{} {}'.format(TC, result))