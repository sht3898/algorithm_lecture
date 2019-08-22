import sys; sys.stdin = open('1210_input.txt', 'r')


def DFS(x, y):
    if x == 0: return y

    arr[x][y] = 0
    if y - 1 >= 0 and arr [x][y - 1]:
        return DFS(x, y - 1)
    elif y + 1 < 100 and arr[x][y + 1]:
        return DFS(x, y + 1)
    else:
        return DFS(x - 1, y)


for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0  # x: 행, y: 열
    # for i in range(100):
    #     if arr[99][i] == 2:
    #         x, y = 99, i
    #         break
    #
    # dir = 0
    # while x:
    #     if dir != 2 and y - 1 >= 0 and arr[x][y-1]:
    #         y, dir = y - 1, 1
    #     elif dir != 1 and y + 1 < 100 and arr[x][y+1]:
    #         y, dir = y + 1, 2
    #     else:
    #         x, dir = x - 1, 0
    # print(y)