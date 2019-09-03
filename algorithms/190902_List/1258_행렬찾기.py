import sys; sys.stdin = open('1258_input.txt', 'r')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        result = []
        if self.head is None:
            return

        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        print(*result)

    def insertlast(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    arr[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]:
            dfs(nx, ny)


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mylist = List()
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                row = 1
                col = 1
                k = i + 1
                while True:
                    if k >= N or arr[k][j] == 0:
                        break
                    if arr[k][j]:
                        k += 1
                        row +=1
                k = j + 1
                while True:
                    if k >= N or arr[i][k] == 0:
                        break
                    if arr[i][k]:
                        k += 1
                        col += 1
                dfs(i, j)
                mylist.insertlast(Node([row * col, row, col]))
    result = []
    cur = mylist.head
    while cur is not None:
        result.append(cur.data)
        cur = cur.next
    result = sorted(result)
    print('#{}'.format(TC), end=' ')
    print(str(len(result)), end='')
    for i in result:
        print(' {} {}'.format(i[1], i[2]), end='')
    print('')
