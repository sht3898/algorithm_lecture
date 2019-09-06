import pprint

# graph = [
#     [],
#     [2, 3, 4],
#     [1, 2],
#     [1, 2, 5],
#     [1, 6],
#     [3, 6],
#     [4, 5]
# ]
#
#
# visit = [False] * (len(graph)+1)
#
# result = []
#
#
# def dfs(x):
#     visit[x] = True
#     result.append(x)
#
#     for w in graph[x]:
#         if not visit[w]:
#             dfs(w)
#
#
# dfs(1)
#
# print(*result)

graph = [
    [0,0,0,0,0],
    [1,1,1,1,0],
    [0,0,0,0,0],
    [0,1,1,1,1],
    [0,0,0,0,0]
]

dx = [0,0,1,-1]
dy = [1,-1,0,0]



visit = [[0]*5 for _ in range(5)]


def dfs(x,y):
    visit[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < 5 and 0<=ny < 5 and not visit[nx][ny] and graph[nx][ny] == 0:
            dfs(nx,ny)

dfs(0,0)

pprint.pprint(visit)
