import sys, itertools
sys.stdin = open("스타트와링크_input.txt")

def DFS(x, s, steam, lteam):
    global mymin
    if mymin == 0: return
    if sum(chk) == N // 2 - 1:
        # print(steam)
        tmp = []
        for i in range(N):
            if chk[i] == 1:
                tmp.append(i)
        comb = list(itertools.combinations(tmp, 2))
        # print(tmp)
        # print(comb)
        for t in comb:
            steam += arr[t[0]][t[1]] + arr[t[1]][t[0]]
        # print(steam)

        tmp = []
        for i in range(N):
            if i == 0: continue
            if chk[i] == 0:
                tmp.append(i)
        comb = list(itertools.combinations(tmp, 2))
        # print(tmp)
        # print(comb)
        for t in comb:
            lteam += arr[t[0]][t[1]] + arr[t[1]][t[0]]
        # print(lteam)
        # print()
        if mymin > abs(steam - lteam):
            mymin = abs(steam - lteam)
            # print(mymin)
        # steam = 0
        # lteam = 0
        return

    for y in range(s, N):
        if x == y: continue
        if chk[y] == 0:
            # print(x)
            # print(y)

            # print(steam)
            # print(steam)
            chk[y] = 1
            DFS(x, y + 1, steam + arr[x][y] + arr[y][x], lteam)
            chk[y] = 0
            if mymin == 0: return

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# chkx = [0] * N
chk = [0] * N
steam = 0
lteam = 0
mymin = 999999999999

DFS(0, 1, 0, 0)
print(mymin)