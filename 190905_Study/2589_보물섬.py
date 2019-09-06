import sys; sys.stdin = open('2589_input.txt', 'r')
import collections

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(v):
    global max_distance
    q = collections.deque()
    q.append(v)
    visited[v[0]][v[1]] = visited_value
    distance = 0
    while q:
        distance += 1
        for _ in range(len(q)):
            v = q.popleft()
            for i in range(4):
                nx, ny = v[0] + dx[i], v[1] + dy[i]
                if 0 <= nx < height and 0 <= ny < width and matrix[nx][ny] == 'L' and visited[nx][ny] < visited_value:
                    visited[nx][ny] = visited_value
                    q.append([nx, ny])
    distance -= 1
    if max_distance < distance:
        max_distance = distance


height, width = map(int, input().split())
matrix = [input() for _ in range(height)]
visited = [[0] * width for _ in range(height)]
visited_value = 0
max_distance = 0
for i in range(height):
    for j in range(width):
        if matrix[i][j] == 'L':
            visited_value += 1
            bfs([i, j])
print(max_distance)
