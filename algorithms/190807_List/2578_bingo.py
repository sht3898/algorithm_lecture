import sys
sys.stdin = open('bingo.txt', 'r')

arr = []
speak = []
result = [[0]*5 for _ in range(5)]
count = 0


for _ in range(5):
    arr.append(list(map(int, input().split())))

for _ in range(5):
    speak += list(map(int, input().split()))

for num in speak:
    bingo = 0
    count += 1
    for a in range(5):
        for b in range(5):
            if arr[a][b] == num:
                result[a][b] = 1

    # 가로&세로
    # for width in result:
    #     if sum(width) == 5:
    #         bingo += 1
    for a in range(5):
        temp1, temp2 = 0, 0
        for b in range(5):
            temp1 += result[a][b]
            temp2 += result[b][a]
        if temp1 == 5:
            bingo += 1
        if temp2 == 5:
            bingo += 1

    # 대각선
    temp1, temp2 = 0,0
    for idx in range(5):
        temp1 += result[idx][4-idx]
        temp2 += result[idx][idx]
        if temp1 == 5:
            bingo += 1
        if temp2 == 5:
            bingo += 1
    # print(result)

    if bingo >= 3:
        print(count)
        break
